class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_str(cls, name_age):
        return cls(name_age.split("_")[0], name_age.split("_")[1])


p = Person('Ashish', 29)
print(p.name)
print(p.age)

p1 = Person.from_str("Ashish_29")
print(p1.name)
print(p1.age)
