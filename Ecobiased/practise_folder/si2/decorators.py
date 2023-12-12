def text_split(func):
    def wrapper():
        result = func()
        return result.split(" ")
    return wrapper()


@text_split
def text_hello():
    return 'Hello I am Ashish'


print(text_hello)


def text_to_lower(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper


@text_to_lower
def hello_text():
    return "I Am Ashish Kumar"


print(hello_text())


def greet(func):
    def wrapper(*args, **kwargs):
        print("good Morning")
        func(*args, **kwargs)
        print("Thanks")
    return wrapper


@greet
def add_number(a, b):
    print(a + b)


add_number(4, 6)


def add_symbol(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + '!'
    return wrapper


def text_l(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper


@add_symbol
@text_l
def hi_text(name):
    return name


print(hi_text('ASHISH'))


