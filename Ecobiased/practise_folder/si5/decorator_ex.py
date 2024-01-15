def text_to_lower(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper

def add_symbol(func):
    def wrapper():
        result = func()
        return result + '!'
    return wrapper

@text_to_lower
def hello_text():
    return "HELLO TEXT"

@add_symbol
def hello_world():
    return "hello world"

@text_to_lower
@add_symbol
def multiple_decorator():
    return 'HELLO WORLD'


print(hello_world())
print(hello_text())
print(multiple_decorator())

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

def text_to_lower1(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper

@text_to_lower1
def hello_name(name):
    return name

print(hello_name('ASHISH'))



