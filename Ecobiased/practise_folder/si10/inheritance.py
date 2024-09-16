# example of single inheritance

class Person:

    def __init__(self, name):
        print("call constructor now")
        self.name = name

    def show(self):
        return f"My name is {self.name}."


class Employee(Person):

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self, salary):
        return f"My name is {self.name} and my salary is {salary}"


p = Employee('Ashish')
print(p.show())
print(p.get_salary(34))


# example of multiple inheritance

class Employee1:
    def __init__(self):
        print("I am from Employee1")


class Employee2:
    def __init__(self):
        print("I am from Employee2")


class MainEmployee(Employee1, Employee2):
    pass


me = MainEmployee()


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
