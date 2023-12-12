from abc import ABC, abstractmethod


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Suv(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Suv'
        print(f"This is a {self.car_type} car.")


class Sedan(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Sedan'
        print(f"This is a {self.car_type} car.")


class Truck(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Truck'
        print(f"This is a {self.car_type} car.")


class FactoryClass:

    def create_factory(self, brand, model, car_type):
        if car_type == 'Sedan':
            return Sedan(brand, model)
        elif car_type == 'Suv':
            return Suv(brand, model)
        elif car_type == 'Truck':
            return Truck(brand, model)
        else:
            return ValueError(f"Unknown car type {car_type}.")


fc = FactoryClass()
print(fc.create_factory('Toyota', 'cramy', 'Sedan'))
print(fc.create_factory('Ford', 'Explorer', 'Suv'))
print(fc.create_factory('Chevrolet', 'Silverado', 'Truck'))


