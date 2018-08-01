from functools import reduce

number = 10

print(reduce(lambda a, n: a * n, range(1, number+1)))