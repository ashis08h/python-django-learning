class MyClass:

    def __init__(self, value):
        self.value = value

    def info(self):
        return self.value

    @property
    def value_of_property(self):
        return self.value*10

    @value_of_property.setter
    def value_of_property(self, new_value):
        self.value = new_value


mc = MyClass(67)
print(mc.info())
print(mc.value_of_property)
mc.value_of_property = 34
print(mc.info())
print(mc.value_of_property)
