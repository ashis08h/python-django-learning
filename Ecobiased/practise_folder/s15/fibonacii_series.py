# example of fibonocci series without recursion

def fibonocci(input_num):
    a, b = 0, 1
    series = []
    for _ in range(input_num):
        series.append(a)
        a, b = b, a+b
    return series


print(fibonocci(10))


# example of fibonocci series with recursion


def generate_fibonocci_series(num):

    if num <= 1:
        return num
    else:
        return generate_fibonocci_series(num-1) + generate_fibonocci_series(num-2)


for i in range(10):
    print(generate_fibonocci_series(i), end=" ")