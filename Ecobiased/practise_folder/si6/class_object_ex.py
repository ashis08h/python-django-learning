class Person:
    name = 'Ashish'
    age = 29
    dob = '30-12-1995'

    def info(self):
        print(f"My name is {self.name} my age is {self.age} and my dob is {self.dob}")


p1 = Person()
print(p1.name)
print(p1.age)
print(p1.dob)
p1.info()