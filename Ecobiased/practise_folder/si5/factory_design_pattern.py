class Car:

    def __init__(self, brand, model):
        self.name = brand
        self.brand = model


class Suv(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Suv'
        print(f"This is from {self.car_type}")


class Sedan(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Sedan'
        print(f"This is from {self.car_type}")


class Truck(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Truck'
        print(f"This is from {self.car_type}")


class FactoryClass:

    def create_instance(self, brand, model, car_type):
        if car_type == 'Suv':
            Suv(brand, model)
        elif car_type == 'Sedan':
            Sedan(brand, model)
        elif car_type == 'Truck':
            Truck(brand, model)
        else:
            return ValueError('Unknown car type')


fc = FactoryClass()
fc.create_instance('toyota', 'toyotamodel', 'Suv')
fc.create_instance('nano', 'nanomodel', 'Sedan')
fc.create_instance('Nexon', 'nexonmodel', 'Truck')
