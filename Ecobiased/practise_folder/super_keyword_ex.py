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


class a:

    def test(self):
        print("a")


class b(a):
    # def test(self):
    #     print("b")
    pass


class c(a):
    # def test(self):
    #     print("c")
    pass


class d(b, c):
    # def test(self):
    #     print("d")
    pass


d().test()


class CustomContextManager:
    def __enter__(self):
        # Code to execute when entering the context
        print("Entering the context")
        return self  # Optionally return something

    def __exit__(self, exc_type, exc_value, traceback):
        # Code to execute when exiting the context
        print("Exiting the context")
        # Handle exceptions if necessary
        if exc_type:
            print(f"Exception occurred: {exc_value}")
        return False  # Return True if you want to suppress the exception, False otherwise

# Usage
with CustomContextManager() as manager:
    print("Inside the context")
