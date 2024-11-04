import threading


class Doubleton:

    __instance = None
    __lock = threading.Lock()
    __count = 0

    def __new__(cls):
        with cls.__lock:
            if cls.__count < 2:
                cls.__instance = super().__new__(cls)
                cls.__count += 1
        return cls.__instance


d1 = Doubleton()
d2 = Doubleton()
d3 = Doubleton()


print(d1 is d2)
print(d2 is d3)
print(d3 is d1)

