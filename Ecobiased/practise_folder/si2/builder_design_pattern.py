class Computer:

    def __init__(self, brand, cpu, ram, storage, graphics_card = None):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.graphics_card = graphics_card

    def __str__(self):
        return f"{self.brand} {self.cpu} {self.ram} {self.storage} {self.graphics_card}"

c = Computer()