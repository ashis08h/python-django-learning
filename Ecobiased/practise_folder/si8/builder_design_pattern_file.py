class Computer:

    def __init__(self, brand, cpu, graphics_card=None):
        self.brand = brand
        self.cpu = cpu
        self.graphics_card = graphics_card

    def __str__(self):
        print(f'My computer brand is {self.brand}, my cpu is {self.cpu} and graphics is {self.graphics_card}')


class BuilderClass:

    def __init__(self, brand):
        self.computer_obj = Computer(brand, "")

    def add_cpu(self, cpu):
        self.computer_obj.cpu = cpu
        return self

    def add_graphics_card(self, graphics):
        self.computer_obj.graphics_card = graphics
        return self

    def build(self):
        return self.computer_obj


bc = BuilderClass('brand1')
bc.add_cpu('cpu1').build()
print(bc)

bc1 = BuilderClass('brand2')
bc1.add_cpu('cpu2').build()
print(bc1)