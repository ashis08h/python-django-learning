class Shape:

    def __init__(self, x, y):
        self.length = x
        self.width = y

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()


s = Shape(5, 3)
print(s.area())
c = Circle(5)
print(c.area())