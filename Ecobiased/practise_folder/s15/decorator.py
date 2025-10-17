def to_lower(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper


@to_lower
def hello_test():
    return "Hello Text"


print(hello_test())


def add_symbol1(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper


def add_symbol2(func):
    def wrapper():
        result = func()
        return result + "$"
    return wrapper


@add_symbol2
@add_symbol1
def say_hello():
    return "Say Hello"


print(say_hello())


def greet(func):
    def wrapper(*args, **kwargs):
        print("Good morning!")
        func(*args, **kwargs)
        print("Thanks!")
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
def subtract_number(a, b):
    return a - b


print(subtract_number(8, 9))


def tag_print(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{tag}] calling function {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@tag_print('DEBUG')
def greet(name):
    print(f"Hello {name}")


greet("Ashish")


def fun1(fun):
    def wrapper():
        print(1)
        result = fun()
        print(1.1)
        return result + '1'
    return wrapper


def fun2(fun):
    def wrapper():
        print(2)
        result = fun()
        print(2.2)
        return result + '2'
    return wrapper


@fun2
@fun1
def fun():
    return 'XYZ'


print(fun())
# the print statement which is before fun() call will print in the same order as decorator assigned.
# the print statement which is after fun() call will print in the fifo order first input first outfut opposite
# to above. and the return statement will execute in the fifo order.


