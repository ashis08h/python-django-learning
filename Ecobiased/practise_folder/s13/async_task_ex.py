import asyncio


async def fetch_data():
    print("started fetching data...")
    await asyncio.sleep(4)
    print("data fetched.")
    return {"data": "some_data"}


async def download_data():
    print("started downloading data...")
    await asyncio.sleep(2)
    print("data downloaded.")
    return "File content"


async def main():

    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(download_data())

    result1 = await task1
    result2 = await task2

    print("result")
    print("result1", result1)
    print("result2", result2)
    print("result end")


asyncio.run(main())