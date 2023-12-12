def add(a, b, *args):
    add_res = a + b
    for item in args:
        add_res += item
    return add_res


print(add(2, 3, 4, 7, 9, 10))


def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


person_info(name="ashish", age=30, city="bangalore")


