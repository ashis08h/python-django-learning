def add_number(a, *args):
    result = a
    for num in args:
        result += num
    return result


print(add_number(2, 3, 4, 5))


def read_content(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")


read_content(name='Ashish', age=29, dob='20-23-2023')