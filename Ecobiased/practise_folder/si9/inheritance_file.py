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


class A:

    # def show(self):
    #     print("I am from show A")
    pass


class B(A):

    # def show(self):
    #     print("I am from show B")
    pass


class C:

    def show(self):
        print("I am from show C")
    pass


class D(A, C):

    # def show(self):
    #     print("I am from show D")
    pass


class E(B, C):

    # def show(self):
    #     print("I am from show D")
    pass

# class MainlyClass(B, C):
#     pass


# class MainlyClass1(C, B):
#     pass
#
#
# mc = MainlyClass()
# mc.show()


# mc = MainlyClass1()
# mc.show()

#
class MainlyClass2(D, B):
    pass


mc = MainlyClass2()
mc.show()