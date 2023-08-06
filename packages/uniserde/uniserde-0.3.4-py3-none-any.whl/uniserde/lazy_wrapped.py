from typing import *  # type: ignore


class LazyWrapped:
    _uniserde_remaining_fields_: Dict[str, Tuple[Any, Callable[[Any], Any]]]

    def __getattr__(self, name: str) -> Any:
        # See if the field is in the remaining fields dict
        try:
            raw_value, deserialize_value = self._uniserde_remaining_fields_.pop(name)
        except KeyError:
            raise AttributeError(name) from None

        # Deserialize it
        parsed_value = deserialize_value(raw_value)

        # Cache it
        vars(self)[name] = parsed_value

        # Return it
        return parsed_value
