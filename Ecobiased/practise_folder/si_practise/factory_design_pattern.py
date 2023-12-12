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
        self.car_type = "Truck"
        print(f"The car type is {self.car_type}")


class FactoryDesignPattern:

    def create_obj(self, car_type, brand, model):
        if car_type == 'Sedan':
            return Sedan(brand, model)
        elif car_type == 'Suv':
            return Suv(brand, model)
        elif car_type == 'Truck':
            return Truck(brand, model)
        else:
            return ValueError(f"Unknown car type {car_type}")


fc = FactoryDesignPattern()
print(fc.create_obj('Sedan', 'Toyota', 'Camry'))
print(fc.create_obj('Suv', 'Ford', 'Explorer'))
print(fc.create_obj('Truck', 'Chevrolet', 'Silverado'))




