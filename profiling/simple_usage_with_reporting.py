from memory_profiler import profile

fp = open("memory_usage_simple_usage.log", "a")


@profile(stream=fp)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b

    return a


if __name__ == '__main__':
    my_func()
    fp.write("================================================\n\n")
    fp.close()
