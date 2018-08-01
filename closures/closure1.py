def multiplier(n):
    def mul(k):
        return n * k
    return mul

mul = multiplier(3)
print(mul(3))

n = 10
mult = lambda k, mul=n: mul * k
print(mult(3))