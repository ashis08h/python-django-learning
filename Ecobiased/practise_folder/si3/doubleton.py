class Doubleton:

    __instance = None
    __count = 0

    def __new__(cls):
        if cls.__count < 2:
            cls.__instance = super().__new__(cls)
            cls.__count += 1
        return cls.__instance


dt1 = Doubleton()
dt2 = Doubleton()
dt3 = Doubleton()

print(dt1 is dt2)
print(dt2 is dt3)
print(dt1 is dt3)


