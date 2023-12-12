class MyClass:

    def __init__(self, value):
        self.value = value

    @property
    def ten_value(self):
        return self.value * 10

    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value/10


mc = MyClass(67)
print(mc.ten_value)
mc.ten_value = 670
print(mc.ten_value)