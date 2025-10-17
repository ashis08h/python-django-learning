import asyncio


# example of async task where main task will wait for completing both the tasks.
# here both the task will start together.
# async def fetch_data():
#     print("started fetching data..")
#     await asyncio.sleep(2)
#     print("fetched data..")
#     return {'data': 'some data'}
#
#
# async def download_data():
#     print("started downloading data..")
#     await asyncio.sleep(5)
#     print("file downloaded")
#     return "file content"
#
#
# async def main():
#     task1 = asyncio.create_task(fetch_data())
#     task2 = asyncio.create_task(download_data())
#
#     result1 = await task1
#     result2 = await task2
#
#     print("result")
#     print("result1", result1)
#     print("result2", result2)
#     print("result end here")
#
#
# asyncio.run(main())


# example of async task where main task will not wait for any task start together

async def my_task(name, delay):
    print(f"Task name {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay} seconds.")


async def main():

    # run concurrently
    await asyncio.gather(
        my_task("A", 2),
        my_task("B", 1),
        my_task("C", 3),
    )


# run the main event loop
asyncio.run(main())