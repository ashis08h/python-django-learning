class Employee:

    def __init__(self):
        print("This is default constructor.")

    def show(self):
        print("This is show.")


class Employee1:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("This is parameterized constructor.")

    def show(self):
        print("This is show.")

e = Employee()
e.show()

e1 = Employee1("Ashish", 23)
e1.show()