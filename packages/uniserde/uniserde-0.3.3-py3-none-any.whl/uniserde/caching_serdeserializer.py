import enum
import inspect
from abc import ABC, abstractmethod
from typing import *  # type: ignore

import uniserde

from . import case_convert, common, serde_class
from .common import SerdeError

IN = TypeVar("IN")
OUT = TypeVar("OUT")

Handler: TypeAlias = Callable[["CachingSerDeserializer[IN, OUT]", IN, Type[OUT]], OUT]


class CachingSerDeserializer(ABC, Generic[IN, OUT]):
    # Types which are passed through without any processing. Must be defined by
    # subclasses.
    _passthrough_types: Set[Type[IN]]

    # Maps types to handlers. This acts as cache for previously seen types. Must
    # be defined by subclasses. (An empty dict is fine.)
    _handler_cache: Dict[Type[IN], Handler]

    # If a method of this name is present in a class (and it isn't the one
    # inherited from `Serde`) this will be used for handling that class, rather
    # than the default behavior.
    _override_method_name: str

    def __init_subclass__(cls) -> None:
        # Add handlers for all of the class's passthrough types
        def make_handler_from_passthrough_type(
            passthrough_type: Type,
        ) -> Handler:
            def result(self, value: IN, as_type: Type[OUT]) -> OUT:
                if not isinstance(value, as_type) and not (
                    isinstance(value, int) and as_type is float
                ):
                    raise SerdeError(f"Expected `{as_type}`, got `{value}`")

                return value  # type: ignore

            return result

        for typ in cls._passthrough_types:
            cls._handler_cache[typ] = make_handler_from_passthrough_type(typ)

    def __init__(
        self,
        *,
        custom_deserializers: Dict[Type, Callable[[IN, Type[OUT]], OUT]] = {},
    ):
        self._custom_deserializers = custom_deserializers

    @abstractmethod
    def _get_class_fields_and_handlers(
        self, value_type: Type
    ) -> Iterable[Tuple[str, str, Callable[[IN, Type], Any]]]:
        """
        Return a list of (python_name, json_name, handler) tuples for each
        field in the class.
        """
        raise NotImplementedError()

    def process(self, value: IN, as_type: Type[OUT]) -> OUT:
        # Special case: rapidly handle simple passthrough types to increase
        # performance
        if as_type in self._passthrough_types:
            if not isinstance(value, as_type) and not (
                isinstance(value, int) and as_type is float
            ):
                raise SerdeError(f"Expected `{as_type}`, got `{value}`")

            return value  # type: ignore

        # Otherwise get a handler and use it
        handler = self._get_handler(as_type)
        return handler(self, value, as_type)

    def _get_handler(
        self,
        value_type: Type,
    ) -> Handler:
        # Prepare the key for the cache lookup
        key = get_origin(value_type)
        if key is None:
            key = value_type

        # Custom handlers take precedence
        try:
            custom_handler = self._custom_deserializers[key]
        except KeyError:
            pass
        else:
            return lambda self, value, as_type: custom_handler(value, as_type)

        # Use a cached handler if possible
        try:
            return self._handler_cache[key]
        except KeyError:
            pass

        # Otherwise create the appropriate handler and cache it for next time
        assert inspect.isclass(value_type), value_type
        handler = self._create_class_handler(value_type)
        self._handler_cache[key] = handler

        return handler

    def _create_class_handler(
        self,
        value_type: Type,
    ) -> Handler:
        # Case: The class has a custom method for handling it
        #
        # This needs care, depending on whether the method was just overwritten
        # as a regular method, or as a static/class method.
        try:
            override_method = getattr(value_type, self._override_method_name)
        except AttributeError:
            pass
        else:
            serde_class_method = getattr(serde_class.Serde, self._override_method_name)

            try:
                override_method_func = override_method.__func__
            except AttributeError:
                override_method_func = override_method

            if override_method_func is not serde_class_method.__func__:
                return lambda self, value, _type: override_method(value, {})

        # Case: Enum
        if issubclass(value_type, enum.Enum):

            def handle_enum(self, value, _type):
                if not isinstance(value, str):
                    raise SerdeError(f"Expected enumeration string, got `{value}`")

                try:
                    py_name = case_convert.camel_case_to_all_upper(
                        value
                    )  # ValueError if not camel case
                    return value_type[py_name]  # ValueError if not in enum
                except KeyError:
                    raise SerdeError(f"Invalid enumeration value `{value}`") from None

            return handle_enum

        # Case: Base which is serialized `@as_child`
        if common.should_serialize_as_child(value_type):
            # Precompute a set of all possible classes
            child_classes_and_handlers_by_doc_name = {
                case_convert.upper_camel_case_to_camel_case(cls.__name__): (
                    cls,
                    self._create_fieldwise_class_handler(cls),
                )
                for cls in common.all_subclasses(value_type, True)
            }

            def handle_as_child(self, value, _type):
                # Look up the real type
                try:
                    type_tag = value.pop("type")
                except KeyError:
                    raise SerdeError(f"Object is missing the `type` field") from None

                # Get the class
                try:
                    (
                        child_class,
                        child_class_handler,
                    ) = child_classes_and_handlers_by_doc_name[type_tag]
                except KeyError:
                    raise SerdeError(
                        f"Encountered invalid type tag `{type_tag}`"
                    ) from None

                # Delegate to that class's handler
                return child_class_handler(self, value, child_class)

            return handle_as_child

        # Case: Regular old class
        return self._create_fieldwise_class_handler(value_type)

    def _create_fieldwise_class_handler(self, value_type: Type) -> Handler:
        handler = FieldwiseClassHandler()

        for py_name, doc_name, field_type in self._get_class_fields_and_handlers(
            value_type
        ):
            handler.add_field(
                py_name,
                doc_name,
                field_type,
                self._get_handler(field_type),
            )

        return handler


class FieldwiseClassHandler:
    fields: List[Tuple[str, str, Type, Handler]]

    def __init__(self):
        self.fields = []

    def add_field(
        self,
        python_name: str,
        doc_name: str,
        field_type: Type,
        handler: Handler,
    ):
        self.fields.append((python_name, doc_name, field_type, handler))

    def __call__(
        self,
        calling_ser_deserializer: CachingSerDeserializer,
        raw: Any,
        value_type: Type,
    ) -> Any:
        # Make sure the raw value is a dict
        if not isinstance(raw, dict):
            raise uniserde.SerdeError(f"Expected object, got `{raw!r}`")

        # Create an instance of the class
        result = object.__new__(value_type)
        result_dict = vars(result)

        # Handle all fields
        for py_name, doc_name, field_type, handler in self.fields:
            # Get the raw value
            try:
                raw_value = raw.pop(doc_name)
            except KeyError:
                raise uniserde.SerdeError(f"Missing field `{doc_name!r}`") from None

            # Process it
            processed_value = handler(calling_ser_deserializer, raw_value, field_type)

            # Store it
            result_dict[py_name] = processed_value

        # Make sure there are no stray fields
        if len(raw) > 0:
            raise SerdeError(
                f"Superfluous object fields `{'`, `'.join(map(str, raw.keys()))}`"
            )

        return result
