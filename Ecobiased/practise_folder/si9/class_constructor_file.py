class Person:

    def __init__(self):
        print('I am from constructor.')

    def info(self):
        print("I am from info method.")


class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("I am from parametrized constructor.")

    def info(self):
        print(f"My name is {self.name} and my age is {self.age}.")


p = Person()
p.info()

p1 = Person1('Ashish', 23)
p1.info()