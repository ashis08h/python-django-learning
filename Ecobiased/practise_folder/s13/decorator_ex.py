def to_lower(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper


@to_lower
def hello_text():
    return "Hello Ashish"


print(hello_text())


def add_symbol1(func):
    def wrapper():
        result = func()
        return result + "@"
    return wrapper


def add_symbol2(func):
    def wrapper():
        result = func()
        return result + "$"
    return wrapper


@add_symbol2
@add_symbol1
def hello_world():
    return "Hello World"


print(hello_world())


def greet(func):
    def wrapper(*args, **kwargs):
        print("Good morning!")
        func(*args, **kwargs)
        print("Thanks!")
    return wrapper


@greet
def add_number(a, b):
    print(a + b)


add_number(2, 3)


def add_extra(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 5
    return wrapper


@add_extra
def subtract_number(a, b):
    return a - b


print(subtract_number(3, 5))

def tag_print(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{tag}] calling function: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@tag_print("DEEBUG")
def greet(name):
    print(f"Hello {name}")


greet("Ashish")


# just for practice


def tag_printer1(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{tag}] function calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@tag_printer1("DEBUG")
def greet1(name):
    print(name)


greet1("Ashish")


