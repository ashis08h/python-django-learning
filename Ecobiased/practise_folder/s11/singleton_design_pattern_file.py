import threading


class Singleton1:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


s1 = Singleton1()
s2 = Singleton1()

print(s1 is s2)


class Singleton2:

    __instance = None

    def __init__(self):
        pass

    @classmethod
    def create_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance


s21 = Singleton2()
s22 = Singleton2()

print(s21.create_instance() is s22.create_instance())


class Singleton3:

    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance


s31 = Singleton3()
s32 = Singleton3()

print(s31 is s32)


class Singleton4:

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


s41 = Singleton4()
s42 = Singleton4()
print(s41.create_instance() is s42.create_instance())