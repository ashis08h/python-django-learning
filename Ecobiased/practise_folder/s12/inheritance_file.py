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


e = Employee('Ashish')
print(e.show())
print(e.get_salary(34))

# example of multiple inheritance


class Employee1:

    def __init__(self):
        print("I am from employee1.")


class Employee2:

    def __init__(self):
        print("I am from employee2.")


class MainEmployee(Employee1, Employee2):
    pass


MainEmployee()

print("*******************")


class A:

    # def show(self):
    #     print("I am from show A.")
    pass


class B:

    def show(self):
        print("I am from show B.")
    pass


class C:

    # def show(self):
    #     print("I am from show C.")
    pass


class D(A, C):
    # def show(self):
    #     print("I am from show D.")
    pass


class E(B, C):
    def show(self):
        print("I am from show E.")


class MainlyClass(B, C):
    pass


class MainlyClass2(C, B):
    pass


class MainlyClass3(B, D):
    pass


class MainlyClass4(D, B):
    pass


# mc = MainlyClass()
# mc.show()

# mc1 = MainlyClass2()
# mc1.show()

# mc2 = MainlyClass3()
# mc2.show()

mc3 = MainlyClass4()
mc3.show()