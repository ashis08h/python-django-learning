class MyClass:

    def __init__(self, value):
        self.value = value

    def show(self):
        return self.value

    @property
    def return_value(self):
        return self.value*10

    @return_value.setter
    def return_value(self, new_value):
        self.value = new_value/10


c = MyClass(64)
print(c.show())

print(c.return_value)

c.return_value = 640
print(c.show())
print(c.return_value)