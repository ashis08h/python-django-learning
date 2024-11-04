class Person:

    name = 'Ashish'
    age = 30
    dob = '30-12-1995'

    def info(self):
        print(f"My name is {self.name} and age is {self.age} and dob is {self.dob}")


p = Person()
print(p.name)
print(p.age)
print(p.dob)
p.info()