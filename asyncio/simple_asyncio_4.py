import random
from time import sleep
import asyncio


# def task(pid):
#     """Synchronous non-deterministic task."""
#     sleep(random.randint(1, 3) * 0.1)
#     print('Task %s done' % pid)


async def task_coro(pid):
    """Coroutine non-deterministic task"""
    await asyncio.sleep(random.randint(0, 2) * 0.1)
    print('Task %s done' % pid)
    return random.choice([True, False, False, False, False, False, False, False, False, False, False, False])


# def synchronous():
#     for i in range(1, 10):
#         task(i)


async def asynchronous():
    tasks = [task_coro(i) for i in range(1, 10)]
    return await asyncio.gather(*tasks)


# print('Synchronous:')
# synchronous()

print('Asynchronous:')
print(asyncio.run(asynchronous()))

