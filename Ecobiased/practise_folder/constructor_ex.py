class Person:

    def __init__(self):
        print("I am in default constructor")

    def info(self):
        print("this is info method.")


p1 = Person()
p1.info()


class Person2:

    def __init__(self, n, a):
        print("I am in parameterized constructor.")
        self.name = n
        self.age = a

    def info(self):
        print(f"My name is {self.name} and my age is {self.age}.")


p2 = Person2("Ashish", 20)
p2.info()

