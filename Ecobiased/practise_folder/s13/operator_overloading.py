class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i, {self.y}j, {self.z}k"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


v1 = Vector(2, 3, 4)
v2 = Vector(5, 3, 2)

print("v1", v1)
print("v2", v2)

print(v1 + v2)