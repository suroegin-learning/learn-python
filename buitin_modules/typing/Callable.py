from typing import Callable


def apply_fn_on_value(
        func: Callable[[str], int],
        value: str,
) -> int:
    return func(value)


def text_length(text: str) -> int:
    return len(text)


result = apply_fn_on_value(
    func=text_length,
    value="Hello sudoers! How are you?!",
)

print(result)