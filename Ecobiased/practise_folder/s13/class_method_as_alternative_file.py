class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_str(cls, name_age_str):
        return cls(name_age_str.split(',')[0], name_age_str.split(",")[1])


p1 = Person("Ashish", 29)
print(p1.name)
print(p1.age)

p2 = Person.from_str("Ashish,29")
print(p2.name)
print(p2.age)