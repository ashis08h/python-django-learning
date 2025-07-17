class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"My name is {self.name} and age is {self.age}"


p = Person('Ashish', 29)
print(p.name)
print(p.age)
print(p.info())