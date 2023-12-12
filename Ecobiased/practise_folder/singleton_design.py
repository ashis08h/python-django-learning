# Singleton class with __new__ dunder method without thread safe.
import threading


class Singleton:

    _instance = None  # private class variable to store the instance.

    def __new__(self):
        if self._instance is None:
            self._instance = super().__new__(self)

        return self._instance


instance1 = Singleton
instance2 = Singleton

print(instance1 is instance2)


# singleton class without thread safe
class Singleton1:

    _instance1 = None

    def __init__(self):
        pass

    @classmethod
    def get_obj(self):
        if self._instance1 is None:
            self._instance1 = self()
        return self._instance1


instance12 = Singleton1.get_obj()
instance13 = Singleton1.get_obj()
print(instance12 is instance13)


# singleton class with thread safe.
class SingletonWithThreadSafe:

    _instance_with_thread = None
    _lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def get_instance_with_thread(self):
        with self._lock:
            if not self._instance_with_thread:
                self._instance_with_thread = self()
        return self._instance_with_thread


instance_with_thread1 = SingletonWithThreadSafe.get_instance_with_thread()
instance_with_thread2 = SingletonWithThreadSafe.get_instance_with_thread()

print(instance_with_thread1 is instance_with_thread2)


# Singleton class with __new__dunder method with thread safe
class SingletonClass:

    _instance_pvt_var = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance_pvt_var is None:
                cls._instance_pvt_var = super().__new__(cls)
        return cls._instance_pvt_var


i1 = Singleton
i2 = Singleton

print(i1 is i2)

