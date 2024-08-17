def add_num(a, *args):
    result = a
    for num in args:
        result += num
    return result


print(add_num(3, 4, 5, 6))


def read_content(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}={value}")


read_content(name='ashish', age='34')