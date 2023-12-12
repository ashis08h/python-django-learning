class Calculator:

    def add_numbers(self, x, y, z=0):
        return x+y+z


cla = Calculator()
print(cla.add_numbers(2, 3))


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


