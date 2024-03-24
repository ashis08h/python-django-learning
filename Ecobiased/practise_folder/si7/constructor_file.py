class Person:

    def __init__(self):
        print('I am from default constructor')

    def show(self):
        print('I am from personal class.')


class Person1:

    def __init__(self, name, age):
        print('I am from parameterized constructor')
        self.name = name
        self.age = age


p = Person()
p.show()
p1 = Person1('Ashish', 24)
