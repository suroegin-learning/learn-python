import random
from time import sleep
import asyncio

import random
from time import sleep
import asyncio


async def task_coro(pid):
    await asyncio.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


async def asynchronous():
    tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1, 10)]
    await asyncio.wait(tasks)


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()