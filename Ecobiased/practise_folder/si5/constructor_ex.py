class Person:

    def __init__(self):
        print("I am in default parameter")

    def show(self):
        print("I am in show methods")


class Person1:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("I am from parameterized constructor.")


p = Person()
p1 = Person1('ashish', 23)