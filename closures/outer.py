def outer():
    """Closure example."""
    def inner():
        inner.y += 1
        return inner.y
    inner.y = 0
    return inner

a = outer()
b = outer()
print(a(), a(), a(), b())
