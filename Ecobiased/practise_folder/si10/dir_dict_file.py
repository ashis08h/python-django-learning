a_list = [1, 2, 3]
print(dir(a_list))
print(help(a_list))


class Person:

    def __init__(self):
        self.name = 'Ashish'
        self.age = 29


p = Person()
print(p.__dict__)
print(p.__dir__())