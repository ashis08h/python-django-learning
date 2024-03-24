class Person:

    __age = 25

    def __init__(self):
        self.__name = 'Ashish'


p = Person()
print(p._Person__age)
print(p._Person__name)