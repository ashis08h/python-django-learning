class Person:
    name = 'Ashish'
    age = 29
    dob = '30-12-1995'

    def info(self):
        print(f"My name is {self.name}, I am {self.age} years old and my dob is {self.dob}")


p = Person()
print(p.name)
print(p.age)
print(p.dob)
p.info()