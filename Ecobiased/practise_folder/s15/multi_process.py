import multiprocessing


def square(num):
    return num**2


# if __name__=='__main__':
#     numbers = [1, 2, 3, 4, 5]
#
#     with multiprocessing.Pool(processes=3) as pool:
#         #result = pool.map(square, numbers)
#         # optionally we can add chunksize param also
#         result = pool.map(square, numbers, chunksize=1)
#     print("result", result)


if __name__=='__main__':
    numbers = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=3) as pool:
        result = pool.map(square, numbers, chunksize=1)
    print("result", result)
