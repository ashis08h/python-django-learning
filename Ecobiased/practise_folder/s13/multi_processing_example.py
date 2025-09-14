import multiprocessing


def square(n):
    print(f"Processing {n}")
    return n*n


if __name__=='__main__':
    numbers = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=3) as pool:
        result = pool.map(square, numbers)
        # optionally we can add chunksize param also
        #result = pool.map(square, numbers, chunksize=1)
    print("squares", result)