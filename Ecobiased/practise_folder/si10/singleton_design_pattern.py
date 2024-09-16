import threading


class Singleton1:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Singleton2:

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

print(s1 is s2)

s11 = Singleton2().create_instance()
s12 = Singleton2().create_instance()

print(s11 is s12)


class Singleton3:

    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance


class Singleton4:

    __instance = None
    __lock = threading.Lock()

    @classmethod
    def create_instance(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = cls()
        return cls.__instance


s21 = Singleton3()
s22 = Singleton3()

print(s21 is s22)

s31 = Singleton4().create_instance()
s32 = Singleton4().create_instance()

print(s31 is s32)