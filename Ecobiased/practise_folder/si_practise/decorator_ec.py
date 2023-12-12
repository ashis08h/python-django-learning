def text_split(func):
    def wrapper():
        hello_text = func()
        return hello_text.split(" ")
    return wrapper()

@text_split
def hello_text():
    return "Hello Text"


print(hello_text)


def text_lower(func):
    def wrapper():
        hi_text = func()
        return hi_text.lower()
    return wrapper()


@text_lower
def hi_text():
    return "Hi Text"


print(hi_text)


def greet(func):
    def wrapper(*args, **kwargs):
        print("Good morning")
        func(*args, **kwargs)
        print("Thanks")
    return wrapper


@greet
def add_number(a, b):
    print(a+b)


add_number(4, 5)


# nested decorator
def add_symbol(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper


def text_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@add_symbol
@text_upper
def greet(name):
    return f"My name is {name}"


print(greet("Ashish"))

