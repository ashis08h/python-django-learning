class Person:
    name = 'Ashish'
    age = 23
    dob = '30-12-1995'

    def info(self):
        print(f"My name is {self.name} and age is {self.age} and my dob is {self.dob}")


p1 = Person()
p1.info()