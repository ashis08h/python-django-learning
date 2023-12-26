def text_to_lower(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper


@text_to_lower
def hello_text():
    return "HELLO text"


print(hello_text)


def add_symbol(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper


@add_symbol
@text_to_lower
def hi_text():
    return "HI Text"


print(hi_text())


def greet(func):
    def wrapper(*args, **kwargs):
        print("Good Morning!")
        func(*args, **kwargs)
        print("Thanks")
    return wrapper


@greet
def add_number(a, b):
    print(a+b)


add_number(3, 5)


def text_to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@text_to_upper
def name_text(name):
    return name


print(name_text('i am ashish kumar.'))