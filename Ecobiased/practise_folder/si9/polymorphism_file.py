# example of method overloading also called it compile time polymorphism.
class Calculator:

    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c

    def add_number(self):
        return self.a + self.b + self.c


c1 = Calculator(2, 3)
c2 = Calculator(2, 3, 4)
print(c1.add_number())
print(c2.add_number())

# example of method overriding also called it run time polymorphism.


class Shape:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
        super().__init__(self.radius, self.radius)

    def area(self):
        return 3.14*super().area()


c = Circle(5)
print(c.area())

sh = Shape(3, 4)
print(sh.area())

