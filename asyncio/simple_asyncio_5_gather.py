"""
asyncio.gather() - Returns a Future instance, allowing high level grouping of tasks
"""

import pprint
import asyncio


async def coro(tag):
    print(">", tag)
    await asyncio.sleep(3)
    print("<", tag)
    return tag


loop = asyncio.get_event_loop()

group1 = asyncio.gather(*[coro("group 1.{}".format(i)) for i in range(1, 6)])

all_groups = asyncio.gather(group1)

results = loop.run_until_complete(all_groups)

loop.close()

pprint.pprint(results)
