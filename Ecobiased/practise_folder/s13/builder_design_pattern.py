class Computer:

    def __init__(self, brand, cpu, graphics=None):
        self.brand = brand
        self.cpu = cpu
        self.graphics = graphics

    def __str__(self):
        return f"My computer brand is {self.brand}, cpu is {self.cpu} and graphics is {self.graphics}"


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


bc = BuilderClass('brand1')
bc.add_cpu('cpu1')
print(bc.build())

bc1 = BuilderClass('brand2')
bc.add_cpu('cpu2').add_graphics('graphics1')
print(bc.build())
