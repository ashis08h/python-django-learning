class Person:

    name = 'Ashish'
    age = 28
    dob = '30-12-1995'

    def info(self):
        return f'My name is {self.name} and my age is {self.age} and dob is {self.dob}'


p = Person()
print(p.name)
print(p.age)
print(p.dob)
print(p.info())