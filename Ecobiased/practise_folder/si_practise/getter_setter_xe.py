class MyClass:

    def __init__(self, value):
        self.value = value

    def show(self):
        return f"The value is {self.value}"

    @property
    def get_value(self):
        return self.value * 10

    @get_value.setter
    def get_value(self, new_val):
        self.value = new_val/10


myclass = MyClass(10)
print(myclass.show())
print(myclass.get_value)
myclass.get_value = 67
print(myclass.get_value)