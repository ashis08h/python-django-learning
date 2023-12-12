class ParentClass:

    def parent_method(self):
        print("This is a parent class method.")


class ChildClass(ParentClass):

    def child_method(self):
        print("This is a child class method.")
        super().parent_method()


c = ChildClass()
c.child_method()
c.parent_method()