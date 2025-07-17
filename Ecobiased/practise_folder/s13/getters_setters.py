class Person:

    def __init__(self, value):
        self.value = value

    def info(self):
        return self.value

    @property
    def value_property(self):
        return self.value * 10

    @value_property.setter
    def value_property(self, new_value):
        self.value = new_value


p = Person(67)
print(p.info())

print(p.value_property)
p.value_property = 34
print(p.info())
print(p.value_property)