class Person:

    __age = 34

    def __init__(self, name):
        self.name = name


p = Person('Ashish')
print(p.name)
print(p._Person__age)