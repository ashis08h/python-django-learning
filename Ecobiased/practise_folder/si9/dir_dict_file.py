a_list = [1, 2, 3, 4]
# print(dir(a_list))
# print(help(a_list))


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Ashish', 29)
print(p.__dict__)
print(p.__dir__())
