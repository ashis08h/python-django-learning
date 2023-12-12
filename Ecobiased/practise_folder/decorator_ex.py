def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning!")
        fx(*args, **kwargs)
        print("Thanks")
    return mfx


@greet
def add_number(a, b):
    print(a+b)


add_number(4, 5)


# decorator with lower case

def convert_to_lower(function):
    def mfx():
        func = function()
        lower_word = func.lower()
        return lower_word
    return mfx


@convert_to_lower
def hello():
    return "Hello World"


print(hello())


# example for split method.
def split_text(function):
    def wrapper():
        func = function()
        splitted_text = func.split(" ")
        return splitted_text
    return wrapper


@split_text
def hello_text():
    return "HI I AM ASHISH."


print(hello_text())





