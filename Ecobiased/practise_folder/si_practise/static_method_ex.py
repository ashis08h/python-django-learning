class Myclass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def add_number(a, b):
        return a + b


mycl = Myclass("Ahish", 30)
print(Myclass.add_number(3, 5))