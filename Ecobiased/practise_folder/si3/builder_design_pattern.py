class Computer:

    def __init__(self, brand, cpu, ram, storage, graphics_card=None):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.graphics_card = graphics_card

    def __str__(self):
        return f"My computer brand is {self.brand} cpu is {self.cpu} ram is {self.ram} storage is {self.storage} and graphics is {self.graphics_card}"


class ComputerBuilder:

    def __init__(self, brand):
        self.computer_obj = Computer(brand, '', '', '', '')

    def set_cpu(self, cpu):
        self.computer_obj.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer_obj.ram = ram
        return self

    def set_storage(self, storage):
        self.computer_obj.storage = storage
        return self

    def set_graphics_card(self, graphics_card):
        self.computer_obj.graphics_card = graphics_card
        return self

    def build(self):
        return self.computer_obj


builder = ComputerBuilder('ABC Computers')
computer1 = builder.set_cpu("Intel i5").set_ram("8GB").set_storage("256GB SSD").build()
print(computer1)
computer2 = builder.set_cpu("Intel i6").set_ram("10GB").set_storage("1TB SSD").set_graphics_card("NVIDIA").build()
print(computer2)
