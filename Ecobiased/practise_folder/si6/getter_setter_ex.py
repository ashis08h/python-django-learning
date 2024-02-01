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


mc = MyClass(64)
print(mc.show())
print(mc.return_value)
mc.return_value = 6400
print(mc.show())
print(mc.return_value)

