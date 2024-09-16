class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def add_number(num1, num2):
        return num1 + num2


m = MyClass('Ashish', 29)
print(m.name)
print(m.age)

print(MyClass.add_number(3, 5))
