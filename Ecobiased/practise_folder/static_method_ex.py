class MyClass:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def add(a, b):
        return a+b


m1 = MyClass(3, 'Ashish')
print(MyClass.add(3, 6))
