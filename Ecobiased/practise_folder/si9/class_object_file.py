class Person:
    name = 'Ashok'
    age = 23
    dob = "20-12-1995"

    def info(self):
        return f"My name is {self.name} and age is {self.age} and dob is {self.dob}"



p = Person()
print(p.name)
print(p.age)
print(p.dob)
print(p.info())