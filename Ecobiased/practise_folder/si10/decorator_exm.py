def to_lower(func):

    def wrapper():
        result = func()
        return result.lower()
    return wrapper


def add_symbol(func):

    def wrapper():
        result = func()
        return result + '!'
    return wrapper


def add_second_symbol(func):

    def wrapper():
        result = func()
        return result + '#'
    return wrapper


def greet(func):

    def wrapper(*args, **kwargs):
        print("Good Morning !")
        func(*args, **kwargs)
        print("Thank you !")
    return wrapper


@greet
def add_number(a, b):
    print(a+b)


add_number(2, 4)


def add_extra(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 10
    return wrapper


@add_extra
def sub_number(a, b):
    return a - b


@add_second_symbol
@add_symbol
def hello_name():
    return "My name is Ashish"


@to_lower
def hello_text():
    return 'Hi I am Ashish'


print(hello_text())
print(hello_name())
print(sub_number(4, 3))




