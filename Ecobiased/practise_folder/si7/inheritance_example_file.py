# Example of Single inheritance.
class Employee:

    def __init__(self, name):
        self.name = name

    def show(self):
        return f"My name is {self.name}."


class Manager(Employee):

    def get_salray(self, salary):
        return f"My salary is {salary}"


m = Manager('Ashish')
print(m.show())
print(m.get_salray(2300))


# example of the multi inheritance.
class Employee1:

    def get_salary(self, salary):
        return f"New salary is {salary}"


class Employee2:

    def get_salary(self, salary):
        return f"New salary1 is {salary}"


class Employee3(Employee2, Employee1):
    pass


e3 = Employee3()
print(e3.get_salary(12))

