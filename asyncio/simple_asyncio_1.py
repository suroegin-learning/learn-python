"""
Корутины могут быть запущены из другой корутины или могут быть запущены с помощью create_task.
После того, как создали список задач, объединяем их с помощью wait.
Затем, отправляем на выполнение через run_until_complete.
"""

import asyncio


async def foo():
    print("Running in foo.")
    await asyncio.sleep(1)
    print("Explicit context switch to foo again.")


async def foo2():
    print("Running in foo2.")
    await asyncio.sleep(1)
    print("Explicit context switch to foo2 again.")


loop = asyncio.get_event_loop()
tasks = [loop.create_task(foo()), loop.create_task(foo2())]
wait_tasks = asyncio.wait(tasks)
loop.run_until_complete(wait_tasks)
loop.close()
