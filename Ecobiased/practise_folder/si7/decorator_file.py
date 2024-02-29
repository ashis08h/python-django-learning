def str_to_lower(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper()


def add_symbol(func):
    def wrapper():
        result = func()
        return result + '!'
    return wrapper()


@str_to_lower
def hello_text():
    return 'I am Ashish'


print(hello_text)


@add_symbol
def hello_text2():
    return 'I am Ashish'


print(hello_text2)


def add_symbol1(func):
    def wrapper():
        result = func()
        return result + '!!'
    return wrapper()


def str_to_upper(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@add_symbol1
@str_to_upper
def name_fun():
    return 'My name is Ashish'


print(name_fun)


def greet(func):
    def wrapper(*args, **kwargs):
        print("good morning!")
        func(*args, **kwargs)
        print("Thanks")
    return wrapper


def add_extra(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('result', result)
        return result + 10
    return wrapper


@greet
def add_number(a, b):
    print(a+b)


add_number(3, 5)


@add_extra
def sub_number(a, b):
    return a-b


print(sub_number(4, 2))
