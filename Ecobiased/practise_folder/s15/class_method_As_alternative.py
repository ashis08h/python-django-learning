class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_str(cls, name_age_str):
        return cls(name_age_str.split("_")[0], name_age_str.split("_")[1])


p = Person("Ashish", 34)
print(p.name)
print(p.age)

p2 = Person.from_str("Ashish_34")
print(p2.name)
print(p2.age)