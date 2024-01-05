class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Sedan(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Sedan'
        print(f"I am in {self.car_type}.")


class Suv(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Suv'
        print(f"I am from {self.car_type}.")


class Truck(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Truck'
        print(f"I am from {self.car_type}.")


class FactoryClass:

    def create_instance(self, brand, model, car_type):
        if car_type == 'Sedan':
            Sedan(brand, model)
        elif car_type == 'Suv':
            Suv(brand, model)
        elif car_type == 'Truck':
            Truck(brand, model)
        else:
            return ValueError("Unknown car type.")


fc = FactoryClass()
fc.create_instance('Toyota', 'cramy', 'Sedan')
fc.create_instance('Ford', 'Explorer', 'Suv')
fc.create_instance('Chevrolet', 'Silverado', 'Truck')
