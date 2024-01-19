class Employee:

    def __init__(self, name):
        self.name = name

    def show(self):
        return f"My name is {self.name}"


class Manager(Employee):

    def get_salary(self, salary):
        return f"My salary is {salary}"


m = Manager("Ashish")
print(m.show())
print(m.get_salary(500))