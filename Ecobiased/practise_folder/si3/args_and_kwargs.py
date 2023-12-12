def calculate(a, b, *args):
    result = a + b
    for item in args:
        result += item
    return result


print(calculate(2, 3, 5))


def person_info(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")


person_info(name='ashish', age=23, sex='Male')