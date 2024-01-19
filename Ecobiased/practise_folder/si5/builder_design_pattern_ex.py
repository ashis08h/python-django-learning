class Computer:

    def __init__(self, brand, cpu, graphics_card=None):
        self.brand = brand
        self.cpu = cpu
        self.graphics_card = graphics_card

    def __str__(self):
        return f"My computer brand is {self.brand}, my cpu is {self.cpu} and graphics is {self.graphics_card}"


class BuilderClass:

    def __init__(self, brand):
        self.computer_obj = Computer(brand, "")

    def add_cpu(self, cpu):
        self.computer_obj.cpu = cpu
        return self

    def add_graphics_card(self, graphics_card):
        self.computer_obj.graphics_card = graphics_card
        return self

    def build(self):
        return self.computer_obj


bc = BuilderClass('brand1')
c1 = bc.add_cpu('cpu1').add_graphics_card('gr1').build()
print(c1)
c2 = bc.add_cpu('cpu2').add_graphics_card('gr2').build()
print(c2)

