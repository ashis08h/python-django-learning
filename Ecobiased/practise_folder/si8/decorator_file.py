def lower_case(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper()


@lower_case
def hello_text():
    return "I am Ashish Kumar"


def add_symbol(func):
    def wrapper():
        result = func()
        return result + '!'
    return wrapper()


@add_symbol
def hello_name():
    return 'Hello I am Ashish Kumar'


print(hello_text)
print(hello_name)


def lower_case1(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper()


def add_symbol1(func):
    def wrapper():
        result = func()
        return result + '#'
    return wrapper


def add_symbol2(func):
    def wrapper():
        result = func()
        return result + '$'
    return wrapper


@lower_case1
@add_symbol2
@add_symbol1
def combined_decorator():
    return 'Hi My name is Ashish Kumar'


print(combined_decorator)


def greet(func):
    def wrapper(*args, **kwargs):
        print("Good morning!")
        func(*args, **kwargs)
        print("Thanks")
    return wrapper


@greet
def add_number(a, b):
    print(a + b)


add_number(2, 4)


def add_extra(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 10
    return wrapper


@add_extra
def sub_number(a, b):
    return a-b


print(sub_number(4, 2))