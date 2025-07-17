# example of single inheritance

class Person:

    def __init__(self, name):
        self.name = name

    def show(self):
        return f"My name is {self.name}"


class Employee(Person):

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self, salary):
        return f"My salary is {salary}"


e = Employee("Ashih")
print(e.show())
print(e.get_salary(30))


# Example of multiple inheritance

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
    def show(self):
        print("I am from show A")
    # pass

class B:
    def show(self):
        print("I am from show B")
    # pass


class C:
    def show(self):
        print("I am from show C")
    pass

class D(A, C):
    # def show(self):
    #     print("I am from show D")
    pass


class E(B, C):
    def show(self):
        print("I am from show E")


class MainClass(B, C):
    pass


mc = MainClass()
mc.show()


class MainlyClass2(C, B):
    pass


mc2 = MainlyClass2()
mc2.show()


class MainlyClass3(B, D):
    pass

mc3 = MainlyClass3()
mc3.show()

class MainlyClass4(D, B):
    pass

mc4 = MainlyClass4()
mc4.show()