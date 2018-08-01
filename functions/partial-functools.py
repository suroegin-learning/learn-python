from functools import partial

def funcPart(a, b):
    return a * b

par3 = partial(funcPart, 3, 5)

print(par3())


# аналогично

class mulFunctor:
    def __init__(self, val1):
        self.val1 = val1

    def __call__(self, val2):
        return self.val1 * val2

func3 = mulFunctor(3)
print(func3(4))