def add_number(a, b, *args):
    res = a + b
    for item in args:
        res += item
    return res


print(add_number(2, 4, 5, 6))


def read_content(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


read_content(name='Ashish', age=28)