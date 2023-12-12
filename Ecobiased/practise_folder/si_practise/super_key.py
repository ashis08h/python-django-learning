class ParentClass:

    def parent_method(self):
        print("I am a parent method.")


class ChildClass(ParentClass):

    def child_method(self):
        print("I am a child method.")
        super().parent_method()


c1 = ChildClass()
c1.child_method()

