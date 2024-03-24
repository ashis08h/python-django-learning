class Computer:

    def __init__(self, brand, cpu, graphics_card=None):
        self.brand = brand
        self.cpu = cpu
        self.graphics_card = graphics_card

    def __str__(self):
        print(f'My computer brand is {self.brand} and cpu is {self.cpu} and graphics is {self.graphics_card}')


class BuilderClass:

    def __init__(self, brand):
        self.computer = Computer(brand, '')

    def add_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def add_graphics_card(self, graphics):
        self.computer.graphics_card = graphics
        return self

    def build(self):
        return self.computer


c1 = BuilderClass('brand1')
c1.add_cpu('cpu1').build()
print(c1)
c2 = BuilderClass('brand2')
c2.add_cpu('cpu2').add_graphics_card('gr1').build()
print(c2)

