def to_lower(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper


def add_symbol(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper


def add_symbol2(func):
    def wrapper():
        result = func()
        return result + '%'
    return wrapper

@add_symbol
@to_lower
def hello_text():
    return 'HELLO TEXT'


@add_symbol
@add_symbol2
def hello_text1():
    return 'HELLO TEXT'


print(hello_text())
print(hello_text1())


def greet(func):
    def wrapper(*args, **kwargs):
        print("good morning!")
        func(*args, **kwargs)
        print("Thank you!")
    return wrapper


@greet
def add_number(a, b):
    print(a+b)


add_number(3, 4)


def to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@to_upper
def hello_world(text):
    return text


print(hello_world("Hi I am ashish."))


