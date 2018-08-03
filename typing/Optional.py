from typing import Optional


def test(a: int, b: Optional[int] = None) -> None:
    print(a, b)
    print(type(a), type(b))


test(10)