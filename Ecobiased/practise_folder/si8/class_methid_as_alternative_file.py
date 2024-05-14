class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_str(cls, name_age):
        return cls(name_age.split('_')[0], name_age.split('_')[1])


p1 = Person('Ashish', 23)
print(p1.name)
print(p1.age)

p2 = Person.from_str('Ashish_23')
print(p2.name)
print(p2.age)