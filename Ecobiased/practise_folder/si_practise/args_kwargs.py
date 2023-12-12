def add_number(a, b, *args):
    res = a + b
    for item in args:
        res += item
    return res


print(add_number(2, 3, 4, 5, 6, 8))


def show_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_dict(name='ashish', age=24)
