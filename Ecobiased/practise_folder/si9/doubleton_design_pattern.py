import threading


class DoubletonDesignPattern:

    __instance = None
    __count = 0
    __lock = threading.Lock()

    def __new__(cls):
        with cls.__lock:
            if cls.__count < 2:
                cls.__instance = super().__new__(cls)
                cls.__count += 1
        return cls.__instance


d1 = DoubletonDesignPattern()
d2 = DoubletonDesignPattern()
d3 = DoubletonDesignPattern()

print(d1 is d2)
print(d2 is d3)
print(d3 is d1)