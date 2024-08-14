class Person:

    __age = 31

    def __init__(self, name):
        self.name = name


p = Person('Ashish')
print(p._Person__age)
print(p.name)
# print(p._p__name)