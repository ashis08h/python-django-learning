# example of compile time polymorphism

class Calculator:

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        print(self.z)

    def calculate_add(self):
        return self.x + self.y + self.z


c = Calculator(2, 3)
#print(c.calculate_add())

c1 = Calculator(3, 4, 5)
#print(c1.calculate_add())

c3 = Calculator(7, 6)

# example of run time polymorphism


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


s = Shape(2, 3)
print(s.area())

c = Circle(5)
print(c.area())