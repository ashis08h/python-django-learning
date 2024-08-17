def lower_text(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper


@lower_text
def hello_text():
    return "I am Ashish"


print(hello_text())


def add_symbol(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper


@add_symbol
def hello_name():
    return 'Hello Name'


print(hello_name())


def add_symbol2(func):
    def wrapper():
        result = func()
        return result + '@'
    return wrapper


@add_symbol2
@lower_text
@add_symbol
def test_decorator_layer():
    return 'Test Layer'


print(test_decorator_layer())


def greet(func):
    def wrapper(*args, **kwargs):
        print("Good Morning!")
        func(*args, **kwargs)
        print("Thanks!")
    return wrapper


@greet
def add_number(a, b):
    print(a+b)


add_number(3, 5)


def sub_num(a, b):
    return a-b
