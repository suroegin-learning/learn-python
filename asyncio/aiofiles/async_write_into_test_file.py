import asyncio
import aiofiles


async def writer(i):
    async with aiofiles.open("test_file.txt", mode="a") as f:
        await f.write(f"Boo! Id: {i}\n")
    print("write done")


async def run():
    tasks = [asyncio.ensure_future(writer(i)) for i in range(1, 50+1)]
    await asyncio.wait(tasks)
    print("all tasks done!")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
