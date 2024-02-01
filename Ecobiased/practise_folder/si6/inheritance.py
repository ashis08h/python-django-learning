class Employee:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'My name is {self.name}')


class Manager(Employee):

    def get_salary(self, salary):
        print(f"My salary is {salary}")


m = Manager('Ashish')
m.get_salary(7)
m.show()


# Example of multiple inheritance.
class Employee1:

    def get_salary(self):
        print("My salary is 9")


class Employee2:

    def get_salary(self):
        print("My salary is 8")


class Employee3(Employee2, Employee1):
    pass


e3 = Employee3()
e3.get_salary()


class Employee4(Employee1, Employee2):

    def get_salary(self):
        print("My salary is 6")
        super().get_salary()


e4 = Employee4()
e4.get_salary()
