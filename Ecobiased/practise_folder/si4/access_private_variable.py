class Person:

    __age = 12

    def __init__(self):
        self.__name = "Ashish"


p = Person()
print(p._Person__name)
print(p._Person__age)
# print(p.__age) This will give error.
