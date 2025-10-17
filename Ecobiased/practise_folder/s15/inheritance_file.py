# example of single inheritance

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
print(e.get_salary(34))


class Employee1:

    def __init__(self):
        print("I am from employee1")


class Employee2:

    def __init__(self):
        print("I am from employee2")


class MainEmployee(Employee2, Employee1):
    pass


main_emp = MainEmployee()


class A:

    # def show(self):
    #     print("I am from A")
    pass


class B:

    def show(self):
        print("I am from B")
    #pass


class C:

    def show(self):
        print("I am from C")
    pass


class P:
    def show(self):
        print("I am from P")
    pass


class D(A, C):

    # def show(self):
    #     print("I am from D")
    pass


class E(B, C):

    def show(self):
        print("I am from E")


# class MainClass(B, C):
#
#     pass
#
#
# mc = MainClass()
# mc.show()
#
#
# class MainClass1(C, B):
#     pass
#
#
# mc1 = MainClass1()
# mc1.show()
#
#
# class MainClass2(B, D):
#     pass
#
#
# mc2 = MainClass2()
# mc2.show()
#
#
# class MainClass3(D, B):
#     pass
#
#
# mc3 = MainClass3()
# pass
#
#
# mc3.show()


class F(D, C):

    # def show(self):
    #     print("I am from F")
    pass


class MainClass3(F, P):
    pass


mc5 = MainClass3()
mc5.show()
