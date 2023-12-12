def string_2_lower(fun):
    def wrapper():
        result = fun()
        return result.lower()
    return wrapper


def add_symbol_at_last(fun):
    def wrapper():
        result = fun()
        return result + '!'
    return wrapper


@add_symbol_at_last
@string_2_lower
def hello_text():
    return 'Hello Text'


print(hello_text())


def greet(fun):
    def wrapper(*args, **kwargs):
        print("Good morning")
        fun(*args, **kwargs)
        print("Thanks")
    return wrapper


@greet
def add_number(a, b):
    print(a + b)


add_number(3, 4)


def string_to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@string_to_upper
def say_hello(input_string):
    return input_string


print(say_hello('Hi I am Ashish.'))

