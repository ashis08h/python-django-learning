class Person:

    def __init__(self):
        print("I am from default constructor.")

    def show(self):
        print("I am from person class.")


class Person1:

    def __init__(self, name):
        print("I am from parameterized constructor.")


p = Person()
p.show()
p1 = Person1('Ashish')
