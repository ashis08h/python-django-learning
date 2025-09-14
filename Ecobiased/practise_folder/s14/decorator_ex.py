def to_lower(fun):
    def wrapper():
        result = fun()
        return result.lower()
    return wrapper


@to_lower
def hello_text():
    return "Hello Text"


print(hello_text())


def add_symbol1(fun):
    def wrapper():
        result = fun()
        return result + "!"
    return wrapper


def add_symbol2(fun):
    def wrapper():
        result = fun()
        return result + "$"
    return wrapper


@add_symbol2
@add_symbol1
def say_hello():
    return "Say Hello"


print(say_hello())


def greet(fun):
    def wrapper(*args, **kwargs):
        print("good morning!")
        fun(*args, **kwargs)
        print("Thanks")
    return wrapper


@greet
def add_number(a, b):
    print(a+b)


add_number(3, 4)


def add_extra(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        return result + 10
    return wrapper


@add_extra
def subtract_number(a, b):
    return a-b


print(subtract_number(4, 6))


def tag_print(tag):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            print(f"[{tag}] calling function: {fun.__name__}")
            result = fun(*args, **kwargs)
            return result
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
        return result+"1"
    return wrapper


def fun2(fun):
    def wrapper():
        print(2)
        result = fun()
        return result+"2"

    return wrapper


@fun2
@fun1
def fun():
    return "xyz"

print(fun())

