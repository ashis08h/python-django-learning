a_list = [1, 2, 3]
print(dir(a_list))
print(help(a_list))

print("**************")


class Person:

    def __init__(self):
        self.name = 'Ashish'
        self.age = 34


p = Person()
print(p.__dict__)
print(p.__dir__())