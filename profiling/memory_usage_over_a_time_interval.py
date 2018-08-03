import time

from memory_profiler import memory_usage


def foo():
    time.sleep(1)


mem_usage = memory_usage(foo, interval=0.1, timeout=None)
print(mem_usage)
