class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Suv(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = "Suv"
        print(f"I am from {self.car_type}")


class Sedan(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = "Sedan"
        print(f"I am from {self.car_type}")


class Truck(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = "Truck"
        print(f"I am from {self.car_type}")


class FactoryClass:

    def create_instance(self, brand, model, car_type):
        if car_type == 'Sedan':
            Sedan(brand, model)
        elif car_type == 'Suv':
            Suv(brand, model)
        elif car_type == 'Truck':
            Truck(brand, model)
        else:
            raise ValueError("Unknown car type.")


fc = FactoryClass()
fc.create_instance('brand1', 'model1', 'Sedan')
fc.create_instance('brand2', 'model2', 'Suv')
fc.create_instance('brand3', 'model3', 'Truck')
