import threading


class Singleton:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton
s2 = Singleton

print(s1 is s2)


class Singleton1:

    _instance1 = None

    def __init__(self):
        pass

    @classmethod
    def get_obj(self):
        if self._instance1 is None:
            self._instance1 = self()
        return self._instance1


s11 = Singleton1.get_obj()
s12 = Singleton1.get_obj()

print(s11 is s12)


class Singleton2:

    _instance2 = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance2 is None:
                cls._instance2 = super().__new__(cls)
        return cls._instance2


s21 = Singleton2
s22 = Singleton2

print(s21 is s22)


class Singleton3:

    _instance3 = None
    _lock1 = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def get_obj1(self):
        with self._lock1:
            if self._lock1 is None:
                self._instance3 = self()
        return self._instance3


s31 = Singleton3.get_obj1()
s32 = Singleton3.get_obj1()

print(s31 is s32)