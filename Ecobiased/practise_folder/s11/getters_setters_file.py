class Person:

    def __init__(self, value):
        self.value = value

    def info(self):
        return self.value

    @property
    def value_object(self):
        return self.value*10

    @value_object.setter
    def value_object(self, new_value):
        self.value = new_value


p = Person(67)
print(p.info())
print(p.value_object)
p.value_object = 37
print(p.info())
print(p.value_object)