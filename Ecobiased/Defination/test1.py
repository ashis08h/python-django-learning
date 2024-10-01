# class Calculator:
#     def add(self, x, y):
#         return x + y
#
#     def substract(self, x, y):
#         return x - y
#
#
# obj = Calculator()
# print(obj.add(2, 3))
# print(obj.substract(5, 4))


class Person:

    name = 'Ram'
    age = '23'
    dob = '2000-12-23'

    def can_talk(self):
        print(f"I can talk")

    def can_walk(self):
        print(f'I acn walk')

    def info(self):
        print(f'My name is {self.name} and my age is {self.age} and my dob is {self.dob}.')


obj = Person()
print(obj.name)
print(obj.age)
print(obj.dob)
obj.info()

obj.can_talk()
obj.can_walk()




