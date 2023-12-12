import threading


class MyClass:

    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


m1 = MyClass()
m2 = MyClass()
print(m1 is m2)


class Singleton:

    __instance1 = None

    def __init__(self):
        pass

    @classmethod
    def create_object(cls):
        if not cls.__instance1:
            cls.__instance1 = cls()
        return cls.__instance1


s1 = Singleton()
s2 = Singleton()

print(s1.create_object() is s2.create_object())


class Singleton1:

    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        with cls.__lock:
            if not cls.__instance:
                cls.__instance = super().__new__(cls)
        return cls.__instance


st1 = Singleton1()
st2 = Singleton1()

print(st1 is st2)


class Singletonthread:

    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        pass

    def create_obj(cls):
        with cls.__lock:
            if cls.__instance:
                cls.__instance = cls
        return cls.__instance


stt1 = Singletonthread()
stt2 = Singletonthread()

print(stt1.create_obj() is stt2.create_obj())