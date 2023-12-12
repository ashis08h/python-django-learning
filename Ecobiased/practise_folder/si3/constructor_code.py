class Employee:
    def __init__(self):
        print("This is default constructor")

    def show(self):
        print("This is show method")


class Employee1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("This is from parameterized constructor.")

    def show(self):
        print(f"This is {self.name} and age is {self.age}")


e1 = Employee()
e1.show()

e2 = Employee1('Ashish', 23)
e2.show()