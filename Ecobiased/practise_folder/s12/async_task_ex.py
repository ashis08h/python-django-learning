import asyncio


# define an async function (coroutine) to simulate a database fetch.
async def fetch_data():
    print("started fetching data...")
    await asyncio.sleep(2) # simulate a network delay.
    print("data fetched!..")
    return {"data": "some_data"}


# define an another async function to simulate downloading a file.
async def download_data():
    print("started downloading the data..")
    await asyncio.sleep(2) # simulate a network delay.
    print("data downloaded!..")
    return "File content.."


# Main async function to run both the tasks.
async def main():
    # schedule both the task to run it concurrently.
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(download_data())

    # await both the task to complete.
    result1 = await task1
    result2 = await task2

    print("result")
    print("Fetched data result", result1)
    print("Download file result", result2)
    print("Result End")


# Run the main function
asyncio.run(main())



