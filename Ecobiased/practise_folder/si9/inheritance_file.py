# example of single inheritance

class Employee:

    def __init__(self, name):
        print("call constructor now.")
        self.name = name

    def show(self):
        return f"My name is {self.name}."


class Manager(Employee):

    def get_saralry(self, salary):
        return f"My salary is {salary}"


print("start here")
m = Manager('Ashish')
print(m.show())
print(m.get_saralry(2300))


# example of multiple inheritance.
class Employee1:
    def __init__(self):
        print("I am from employee1.")


class Employee2:
    def __init__(self):
        print("I am from employee2.")


class EmployeeMain(Employee2, Employee1):
    pass


em = EmployeeMain()