class Computer:

    def __init__(self, brand, cpu, graphics=None):
        self.brand = brand
        self.cpu = cpu
        self.graphics = graphics

    def __str__(self):
        return f"My brand is {self.brand} and cpu is {self.cpu} and graphics is {self.graphics}"


class BuilderClass:

    def __init__(self, brand):
        self.computer_obj = Computer(brand, "")

    def add_cpu(self, cpu):
        self.computer_obj.cpu = cpu
        return self

    def add_graphics(self, graphics):
        self.computer_obj.graphics = graphics
        return self

    def build(self):
        return self.computer_obj


bc1 = BuilderClass('brand1')
bc1.add_cpu('cpu1').build()
print(bc1)

bc2 = BuilderClass('brand2')
bc2.add_cpu('cpu2').add_graphics('graphics').build()
print(bc2)