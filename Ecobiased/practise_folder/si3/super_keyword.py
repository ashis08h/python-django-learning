class ParentClass:

    def parent_method(self):
        print("I am from parent method.")


class ChildClass(ParentClass):

    def child_method(self):
        print("I am from child method")
        super().parent_method()


c = ChildClass()
c.child_method()