class Person:

    name = 'Ashish'
    age = 29
    dob = '30-12-1995'

    def info(self):
        return f'My name is {self.name} and age is {self.age} and {self.dob}'


p1 = Person()
print(p1.name)
print(p1.age)
print(p1.dob)
print(p1.info())