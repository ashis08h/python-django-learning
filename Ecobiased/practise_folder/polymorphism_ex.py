# Example of compile time polymorphism or method overloading.
class Calculator:
    def add(self, x, y, z=0):
        return x + y + z


c = Calculator()
print(c.add(3, 4))
print(c.add(2, 4, 5))


# Example of run time polymorphism or method overloading.
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


c = Circle(4)
print(c.area())