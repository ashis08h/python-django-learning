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
    def get_obj(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance


sl1 = Singleton1()
sl2 = Singleton1()
print(sl1.get_obj() is sl2.get_obj())


class Singleton2:

    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance


sm1 = Singleton2()
sm2 = Singleton2()

print(sm1 is sm2)


class Singleton3:

    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def get_obj(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = cls()
        return cls.__instance


sn1 = Singleton3
sn2 = Singleton3
print(sn1 is sn2)
