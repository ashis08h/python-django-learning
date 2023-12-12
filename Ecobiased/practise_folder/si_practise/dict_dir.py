a = [1,2,3]

print(dir(a))

print(help(a))


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('ashish', 23)

print(p1.__dict__)
print(p1.__dir__())