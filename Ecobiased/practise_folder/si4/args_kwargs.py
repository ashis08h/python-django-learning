def add_num(a, b, *args):
    result = a + b
    for item in args:
        result = result + item
    return result


print(add_num(2, 3, 1, 7, 9))


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info(name="Ashish", age=20, dob='30-12-1995')
