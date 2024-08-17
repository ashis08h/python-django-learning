class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_str(cls, to_str):
        return cls(to_str.split("_")[0], to_str.split("_")[1])


p1 = Person('Ashish', 30)
print(p1.name)
print(p1.age)

p2 = p1.from_str("Ashish_30")
print(p2.name)
print(p2.age)