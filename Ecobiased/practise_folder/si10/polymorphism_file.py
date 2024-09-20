# example of method overloading

class Calculator:

    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c

    def add_number(self):
        return self.a + self.b + self.c


c = Calculator(2, 3)
c1 = Calculator(4, 5, 6)
print(c.add_number())
print(c1.add_number())


# example of method overriding.


class Shape:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):

    def __init__(self, radius):
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()


c = Circle(5)
print(c.area())

s = Shape(2, 3)
print(s.area())