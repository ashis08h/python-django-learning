def add_number(a, b, *args):
    result = a + b
    for item in args:
        result += item
    return result


calculator = add_number(2, 3, 4, 5)
print(calculator)


def read_element(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


my_element = read_element(name='ashish', age=23)