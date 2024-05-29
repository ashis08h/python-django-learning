import threading
class Singleton:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)


class Singleton1:

    __instance = None

    def __init__(self):
        pass

    @classmethod
    def create_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance


s1 = Singleton1()
s2 = Singleton1()

print(s1.create_instance() is s2.create_instance())


class Singleton2:

    __lock = threading.Lock()
    __instance = None

    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance


s1 = Singleton2()
s2 = Singleton2()
print(s1 is s2)


class Singleton3():

    __instance = None
    __lock = threading.Lock()

    @classmethod
    def create_instance(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = cls()
        return cls.__instance


s1 = Singleton3()
s2 = Singleton3()
print(s1.create_instance() is s2.create_instance())