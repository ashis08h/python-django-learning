class Person:

    __age = 26

    def __init__(self):
        self.__name = 'Ashish Kumar'


p = Person()
print(p._Person__age)
print(p._Person__name)