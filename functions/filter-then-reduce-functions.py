from functools import reduce

alist = [2, None, 5, None, None, None, 11, None]

print(
    reduce(
        lambda a, n: a * n,
        filter(
            lambda x: x,
            alist
        )
    )
)
