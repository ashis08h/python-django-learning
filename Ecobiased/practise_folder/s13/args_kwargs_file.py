def add_number(a, *args):
    result = a
    for num in args:
        result += num
    return result


print(add_number(2, 3, 4, 5, 6))


def read_value(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}={value}")


read_value(Name='Ashish', Age=20, School=34)
