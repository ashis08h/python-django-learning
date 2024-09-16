class MyClass:

    def __init__(self, value):
        self.value = value

    def info(self):
        return self.value

    @property
    def value_of_class(self):
        return self.value*10

    @value_of_class.setter
    def value_of_class(self, new_value):
        self.value = new_value


m = MyClass(36)
print(m.info())
print(m.value_of_class)

m.value_of_class = 34
print(m.info())
print(m.value_of_class)
