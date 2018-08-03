import asyncio
import aiohttp


async def getter_coro(api_address):
    print(f"Started getter. Link: {api_address}")
    await asyncio.sleep(1)
    async with aiohttp.ClientSession() as session:
        async with session.get(api_address) as resp:
            print(resp.status)
            return len(await resp.text())


loop = asyncio.get_event_loop()

coro_results = asyncio.gather(*[getter_coro(api_address) for api_address in [
    "https://api.coinmarketcap.com/v2/listings/",
    "https://wex.nz/api/3/info",
    "https://blockchain.info/ticker"
]])

loop.run_until_complete(coro_results)
loop.close()

print(coro_results)

results = coro_results.result()
print(results)
print(type(results))