class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def add_number(a, b):
        return a + b


print(MyClass.add_number(3, 5))