class MyClass:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def add_number(a, b):
        return a + b


mc = MyClass(2, 'Ashish')
print(mc.id)
print(mc.name)

print(MyClass.add_number(2, 4))
