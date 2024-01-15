a_list = [1, 2, 3, 4]
print(dir(a_list))

print(help(a_list))

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Ashish', 29)

print(p1.__dict__)
print(p1.__dir__())
