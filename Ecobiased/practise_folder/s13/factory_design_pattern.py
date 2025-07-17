from abc import ABC


class Car(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Suv(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        car_type = "Suv"
        print(f"I am from {car_type}")


class Sedan(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        car_type = "Sedan"
        print(f"I am from {car_type}")


class Truck(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        car_type = "Truck"
        print(f"I am from {car_type}")


class FactoryClass:

    def create_instance(self, car_type, brand, model):
        if car_type == "Suv":
            Suv(brand, model)
        elif car_type == "Sedan":
            Sedan(brand, model)
        elif car_type == "Truck":
            Truck(brand, model)
        else:
            raise ValueError("Unknown car type")


fc = FactoryClass()
fc.create_instance('Sedan', 'brand1', 'model1')
fc.create_instance('Suv', 'brand2', 'model2')
fc.create_instance('Truck', 'brand3', 'model3')
# fc.create_instance('toto', 'brand4', 'model4') raise unkown car type.