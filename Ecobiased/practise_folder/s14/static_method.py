class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def add_number(num1, num2):
        return num1 + num2


mc = MyClass("Ashish", 29)
print(mc.name)
print(mc.age)

print(mc.add_number(5, 6))

print(MyClass.add_number(2, 3))