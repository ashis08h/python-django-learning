class Person:

    def __init__(self):
        print("Hey I am in constructor.")


class Manager:

    def __init__(self, n, o):
        print("Hey I am in Manager class constructor.")
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")


class Car:

    def __init__(self, c, p):
        print("I am in car constructor.")
        self.colour = c
        self.price = p

    def info(self, model):
        print(f"My car colour is {self.colour} and price is {self.price} and model name is {model}")


manager1 = Manager("Ashish", "Software developer")
manager2 = Manager("Rishika", "House Wife")
person1 = Person()
manager1.info()
manager2.info()
car1 = Car("Red", 120)
car1.info("mod1-23")
