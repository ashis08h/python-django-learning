class DoubleTon:

    __instance = None
    __count = 0

    def __new__(cls):
        if cls.__count < 2:
            cls.__instance = super().__new__(cls)
            cls.__count += 1
        return cls.__instance


d1 = DoubleTon()
d2 = DoubleTon()
d3 = DoubleTon()

print(d1 is d2)
print(d2 is d3)
print(d1 is d3)
