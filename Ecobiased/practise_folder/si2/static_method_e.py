class Calculator:

    def __init__(self, id, name):
        self.id = id
        self.name =name

    @staticmethod
    def add(a, b):
        return a + b


c = Calculator(1, 'ashish')
print(Calculator.add(6, 7))