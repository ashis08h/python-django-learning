# example of compile time polymorphism or method overloading.

class Calculator:

    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c

    def add_number(self):
        return self.a + self.b + self.c


c1 = Calculator(1, 2)
c2 = Calculator(1, 2, 3)
print(c1.add_number())
print(c2.add_number())


# example of method overriding, run time polymorphism.


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


s = Shape(2, 4)
print(s.area())

c = Circle(5)
print(c.area())
