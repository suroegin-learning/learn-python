def spam(x, y):
    print(
        "param1 = {}, param2 = {}".format(x, y)
    )

spam1 = lambda x: lambda y: spam(x, y)

def spam2(x):
    def new_spam(y):
        return spam(x, y)
    return new_spam

spam1(2)(3)
spam2(2)(3)
