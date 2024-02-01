class Myclass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def add_number(a, b):
        return a+b


mc = Myclass('Ashish', 29)
print(mc.add_number(3, 4))