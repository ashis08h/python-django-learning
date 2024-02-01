class Parent:

    def parent_method(self):
        print("I am from parent method.")


class Child(Parent):

    def child_method(self):
        print("I am from child method.")
        super().parent_method()


c = Child()
c.child_method()
