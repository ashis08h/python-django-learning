class Computer:

    def __init__(self, brand, cpu, ram, storage, graphics_card=None):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.graphics_card = graphics_card

    def __str__(self):
        return f"My computer brand is {self.brand}, cpu is {self.cpu}, ram is {self.ram}, storage is {self.storage}, graphics is {self.graphics_card}"


class BuilderClass:

    def __init__(self, brand):
        self.computer_obj = Computer(brand, '', '', '', '')

    def add_cpu(self, cpu):
        self.computer_obj.cpu = cpu
        return self

    def add_ram(self, ram):
        self.computer_obj.ram = ram
        return self

    def add_storage(self, storage):
        self.computer_obj.storage = storage
        return self

    def add_graphics_card(self, graphics_card):
        self.computer_obj.graphics_card = graphics_card
        return self

    def build(self):
        return self.computer_obj


bc = BuilderClass('ABC Computers')
c1 = bc.add_cpu('Intel I5').add_ram("8GB").add_storage('256 SSD').build()
print(c1)
c2 = bc.add_cpu('Intel I7').add_ram("18GB").add_storage('356 SSD').add_graphics_card('NVIDIA').build()
print(c2)
