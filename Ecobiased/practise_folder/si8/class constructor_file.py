class Person:

    def __init__(self):
        print('I am from default constructor.')

    def info(self):
        print('I am from person class info method.')


class Person1:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('I am from parameterized constructor.')


p = Person()
p.info()

p1 = Person1('Ashish', 23)
