class Person:

    name = 'Ashish'
    age = 28
    dob = '20-12-1995'

    def info(self):
        print(f"My name is {self.name} and age is {self.age} and my dob is {self.dob}")


p = Person()
print(p.name)
print(p.age)
print(p.dob)
p.info()