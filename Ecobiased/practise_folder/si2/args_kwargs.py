def add_num(a, b, *args):
    result = a + b
    for item in args:
        result += item
    return result


print(add_num(2, 3, 4, 5, 6))


def get_key_value(**kwargs):
    for key, item in kwargs.items():
        print(f"{key}: {item}")


get_key_value(name = 'ashish', age = 23, dob = '345')