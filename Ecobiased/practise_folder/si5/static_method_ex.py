class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def add_number(a, b):
        return a+b


mc = MyClass('ashish', 29)
print(MyClass.add_number(2, 3))
