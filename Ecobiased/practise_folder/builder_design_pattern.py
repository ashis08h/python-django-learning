class Computer:

    def __init__(self, brand, cpu, ram, storage, graphics_card=None):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.graphics_card = graphics_card

    def __str__(self):
        return f"{self.brand} Computer - CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, Graphics Card: {self.graphics_card}"


class ComputerBuilder:
    def __init__(self, brand):
        self.computer = Computer(brand, cpu="", ram="", storage="")
        text = ""

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_graphics_card(self, graphics):
        self.computer.graphics_card = graphics
        return self

    def build(self):
        return self.computer


builder = ComputerBuilder('ABC Computers')
computer1 = builder.set_cpu("Intel i5").set_ram("8GB").set_storage("256GB SSD").build()
print(computer1)

computer2 = builder.set_cpu("AMD Ryzen 7").set_ram("16GB").set_storage("1TB HDD").set_graphics_card("NVIDIA GTX 1650").build()
print(computer2)


