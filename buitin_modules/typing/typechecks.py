import typing


def foo(a: int, b: int) -> None:
    print(a, b)
    return "LOL"


foo(5, "5")

# Now launch mypy tool to find this mistakes in types!