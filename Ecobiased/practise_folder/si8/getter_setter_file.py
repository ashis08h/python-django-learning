class MyClass:

    def __init__(self, value):
        self.value = value

    def info(self):
        return self.value

    @property
    def custom_value(self):
        return self.value*10

    @custom_value.setter
    def custom_value(self, new_value):
        self.value = new_value/10


mc = MyClass(67)
print(mc.info())
print(mc.custom_value)
mc.custom_value = 56
print(mc.info())
print(mc.custom_value)