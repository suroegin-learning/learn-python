import time
import asyncio

start = time.time()


def tic():
    return f"at {time.time() - start} seconds"


async def gr1():
    print(f"gr1 started work: {tic()}")
    await asyncio.sleep(2)
    print(f"gr1 ended work: {tic()}")


async def gr2():
    print(f"gr2 started work: {tic()}")
    await asyncio.sleep(2)
    print(f"gr2 ended work: {tic()}")


async def gr3():
    print(f"Let's do some stuff while the coroutines are blocked, {tic()}")
    await asyncio.sleep(1)
    print("Done!")


loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(gr1()),
    loop.create_task(gr2()),
    loop.create_task(gr3())
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()