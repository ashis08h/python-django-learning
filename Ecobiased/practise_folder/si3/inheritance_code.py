class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"My name is {self.name} and my age is {self.age}"


class Manager(Employee):

    def show_salary(self, salary):
        return f"Manager's salary is {salary}"


m1 = Manager('aSHISH', 20)
print(m1.show())
print(m1.show_salary(2000))