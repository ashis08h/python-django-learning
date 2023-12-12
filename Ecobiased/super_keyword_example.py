class ParentClass:

    def parent_method(self):
        print("This is a parent method.")


class ChildClass(ParentClass):

    def child_method(self):
        print("This is a child method.")
        super().parent_method()

    def parent_method(self):
        print("this is a parent method present in child class.")


c1 = ChildClass()
c1.child_method()
c1.parent_method()


class Employee:

    def __init__(self, name, id):
        self.id = id
        self.name = name


class Programmer(Employee):

    def __init__(self, name, id, language):
        self.lang = language
        super().__init__(name, id)


p1 = Programmer('ashish', 2, 'Python')
print(p1.name)
print(p1.id)
print(p1.lang)