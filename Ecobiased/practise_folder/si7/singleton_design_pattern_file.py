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


s11 = Singleton1()
s12 = Singleton1()
print(s11.create_instance() is s12.create_instance())


class Singleton2:

    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance


s31 = Singleton2()
s32 = Singleton2()
print(s31 is s32)


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


s41 = Singleton3()
s42 = Singleton3()

print(s41.create_instance() is s42.create_instance())