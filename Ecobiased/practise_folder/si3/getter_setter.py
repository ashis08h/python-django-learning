class MyClass:

    def __init__(self, value):
        self.value = value

    def show(self):
        return f"The value is {self.value}"

    @property
    def return_value(self):
        return self.value * 10

    @return_value.setter
    def return_value(self, new_value):
        self.value = self.value / 100


c1 = MyClass(67)
print(c1.show())
print(c1.return_value)
c1.return_value = 67
print(c1.show())
print(c1.return_value)