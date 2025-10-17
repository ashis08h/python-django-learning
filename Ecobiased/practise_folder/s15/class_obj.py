class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"My name is {self.name} and {self.age}"


p = Person("Ashish", 29)
print(p.info())