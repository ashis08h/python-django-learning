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
    def create_object(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance


s11 = Singleton1()
s12 = Singleton1()

print(s11.create_object() is s12.create_object())


class Singleton2:

    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance


s21 = Singleton2()
s22 = Singleton2()

print(s21 is s22)


class Singleton3:

    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def create_obj(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = cls()
        return cls.__instance


s31 = Singleton3()
s32 = Singleton3()

print(s31.create_obj() is s32.create_obj())
