class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


v1 = Vector(2, 3, 4)
print(v1)
v2 = Vector(3, 4, 5)
print(v2)
print(v1+v2)