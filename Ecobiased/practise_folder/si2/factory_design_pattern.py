class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Sedan(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Sedan'
        print(f"The car type is {self.car_type}")


class Suv(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Suv'
        print(f"The car type is {self.car_type}")


class Truck(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Truck'
        print(f"The car type is {self.car_type}")


class FactoryClass:

    def create_object(self, car_type, brand, model):

        if car_type == 'Sedan':
            return Sedan(brand, model)
        elif car_type == 'Suv':
            return Suv(brand, model)
        elif car_type == 'Truck':
            return Truck(brand, model)
        else:
            return ValueError(f"Unknown {car_type}")


fc = FactoryClass()
fc.create_object('Sedan', 'Toyota', 'camry')
fc.create_object('Suv', 'Ford', 'Explorer')
fc.create_object('Truck', 'Chevrelot', 'Silverado')


