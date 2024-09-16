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


s1 = Doubleton()
s2 = Doubleton()
s3 = Doubleton()

print(s1 is s2)
print(s2 is s3)
print(s3 is s1)