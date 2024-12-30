import asyncio


# Define an async function (coroutine) to simulate a database fetch.
async def fetch_data():
    print("start fetching data...")
    await asyncio.sleep(2) # simulate a network delay
    print("data fetched!")
    return {'data': 'some data'}


# Define another async function to simulate downloading a file.
async def download_data():
    print("Start downloading file...")
    await asyncio.sleep(3) # simulate a longer network delay
    print("File downloaded!")
    return "File content"


# Main async function to run both the tasks
async def main():
    # schedule both task to run concurrently
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(download_data())

    # await both the task to complete
    result1 = await task1
    result2 = await task2

    # Use the results
    print("Results:")
    print("Fetch data result:", result1)
    print("Download File Result:", result2)
    print("ResultsEnd:")


# Run the main function
asyncio.run(main())