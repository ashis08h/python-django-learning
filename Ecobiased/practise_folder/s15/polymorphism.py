# example of method overloading
class Calculator:

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def add_number(self):
        return self.x + self.y + self.z


c = Calculator(2, 3)
print(c.add_number())

c1 = Calculator(3, 4, 5)
print(c1.add_number())


# example of method overriding


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
        return 3.14 * self.radius * self.radius


sh = Shape(2, 3)
print(sh.area())

cir = Circle(5)
print(cir.area())