def add_number(a, b, *args):
    result = a + b
    for num in args:
        result += num
    return result


print(add_number(2, 3, 4, 5))


def read_content(**kwargs):

    for key, value in kwargs.items():
        print(f"Key is {key} and value is {value}")


read_content(Name='Ashish', Address='Bangalore', Dob='30-12-1995')