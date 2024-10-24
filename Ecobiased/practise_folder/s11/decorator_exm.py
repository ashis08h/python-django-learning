def to_lower(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper


@to_lower
def hello_text():
    return 'Ashish Kumar'


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


@add_second_symbol
@add_symbol
def hello_world():
    return 'Hello World'


# print(hello_text())
# print(hello_world())


def greet(func):
    def wrapper(*args, **kwargs):
        print("Good Morning!")
        func(*args, **kwargs)
        print("Thanks!")
    return wrapper


@greet
def add_number(a, b):
    print(a + b)


def add_extra(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 10
    return wrapper


@add_extra
def sub_number(a, b):
    return a - b


print(sub_number(4, 2))
#add_number(4, 5)