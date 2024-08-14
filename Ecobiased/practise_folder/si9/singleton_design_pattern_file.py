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


s11 = Singleton1().create_instance()
s12 = Singleton1().create_instance()

print(s11 is s12)


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
    def create_instance(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = cls()
        return cls.__instance


s31 = Singleton3().create_instance()
s32 = Singleton3().create_instance()
print(s31 is s32)