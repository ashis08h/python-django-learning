# example of single inheritence

class Person:

    def __init__(self, name):
        self.name = name

    def show(self):
        return f"My name is {self.name}"


class Employee(Person):

    def get_salary(self, new_salary):
        return f"My new salary is {new_salary}"


e = Employee("Ashish")
print(e.show())
print(e.get_salary(23))

# example of multiple inheritence


class Employee1:

    def __init__(self):
        print("I am from employee1")


class Employee2:

    def __init__(self):
        print("I am from employee2")


class MainEmployee(Employee1, Employee2):
    pass


me = MainEmployee()


class A:

    # def show(self):
    #     print("I am from A")
    pass


class B:

    def show(self):
        print("I am from B")
    #pass


class C:

    # def show(self):
    #     print("I am from C")
    pass


class D(A, C):

    # def show(self):
    #     print("I am from D")
    pass


class E(B, C):

    def show(self):
        print("I am from E")


class MainClass(B, C):
    pass


mc = MainClass()
mc.show()


class MainClass2(C, B):
    pass


mc = MainClass2()
mc.show()


class MainClass3(B, D):
    pass


mc = MainClass3()
mc.show()


class MainClass4(D, B):
    pass


mc = MainClass4()
mc.show()
