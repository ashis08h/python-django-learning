# Example of single inheritance

class Person:

    def __init__(self, name):
        self.name =  name
        print("call constructor.")

    def show(self):
        print(f"My name is {self.name}")


class Employee(Person):

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self, salary):
        print(f"Name is {self.name} and salary is {salary}")


e = Employee('Ashish')
e.show()
e.get_salary(45)

# example of multiple inheritance


class Employee1:

    def __init__(self):
        print("I am from employee1.")


class Employee2:

    def __init__(self):
        print("I am from employee2.")


class MainEmployee(Employee2, Employee1):
    pass


MainEmployee()


class A:

    # def show(self):
    #     print("I am from show A.")
    pass


class B(A):

    # def show(self):
    #     print("I am from show B.")
    pass


class C:

    def show(self):
        print("I am from show C.")
    #pass


class D(A, C):

    # def show(self):
    #     print("I am from show D.")
    pass


class E(B, C):

    def show(self):
        print("I am from show E.")


class MainlyClass(B, C):
    pass


class MainlyClass1(C, B):
    pass


# mc = MainlyClass()
# mc.show()
#
# mc1 = MainlyClass1()
# mc1.show()


class MainlyClass2(D, B):
    pass


# mc2 = MainlyClass2()
# mc2.show()


class MainlyClass3(B, D):
    pass


mc3 = MainlyClass3()
mc3.show()