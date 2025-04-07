def to_lower(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper()


@to_lower
def hello_text():
    return "Ashish Kumar"


print(hello_text)


def add_symbol_1(func):
    def wrapper():
        result = func()
        return result + '!'
    return wrapper


def add_symbol_2(func):
    def wrapper():
        result = func()
        return result + "&"
    return wrapper


@add_symbol_1
@add_symbol_2
def hello_world():
    return "Hello World"


print(hello_world())


def greet(func):
    def wrapper(*args, **kwargs):
        print("Good Morning!")
        func(*args, **kwargs)
        print("Thanks")
    return wrapper


@greet
def add_number(a, b):
    print(a + b)


add_number(3, 4)


def add_extra(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 5
    return wrapper


@add_extra
def sub_number(a, b):
    return a - b


print(sub_number(3, 4))
