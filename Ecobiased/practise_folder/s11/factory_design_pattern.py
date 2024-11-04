from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Suv(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Suv'
        print(f"I am from {self.car_type}")


class Sedan(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Sedan'
        print(f"I am from {self.car_type}")


class Truck(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Truck'
        print(f"I am from {self.car_type}")


class FactoryClass:

    def create_instance(self, car_type, brand, model):
        if car_type == 'Suv':
            Suv(brand, model)
        elif car_type == 'Sedan':
            Sedan(brand, model)
        elif car_type == 'Truck':
            Truck(brand, model)
        else:
            raise ValueError(f"Unknown {car_type}")


fc = FactoryClass()
fc.create_instance('Sedan', 'brand1', 'model1')
fc.create_instance('Suv', 'brand2', 'model2')
fc.create_instance('Truck', 'brand3', 'model3')