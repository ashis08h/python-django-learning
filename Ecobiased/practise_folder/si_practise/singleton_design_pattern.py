import threading


def text_lower(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper


@text_lower
def greet(name):
    return f"My name is {name}"


print(greet('Ashish'))


class MyClass:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


singleton1 = MyClass()
singleton2 = MyClass()

print(singleton1 == singleton2)


class Singleton:

    __instance1 = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls.__instance1 is None:
            cls.__instance1 = cls()
        return cls.__instance1


s1 = Singleton()
s2 = Singleton()
print(s1.get_instance() is s2.get_instance())


class ThreadSingleton:

    __instance_thread = None
    lock = threading.Lock()

    def __new__(cls):
        with cls.lock:
            if cls.__instance_thread is None:
                cls.__instance_thread = super().__new__(cls)
        return cls.__instance_thread


st1 = ThreadSingleton()
st2 = ThreadSingleton()

print(st1 is st2)


class ThreadSingleton:

    __instance2 = None
    _lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def get_obj(cls):
        with cls._lock:
            if not cls.__instance2:
                cls.__instance2 = cls()
        return cls.__instance2


sty1 = ThreadSingleton()
sty2 = ThreadSingleton()

print(sty1.get_obj() is sty2.get_obj())







