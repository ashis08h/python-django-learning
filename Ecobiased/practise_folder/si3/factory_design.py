class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Sedan(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Sedan'
        print(f"This is {self.car_type} car.")


class Suv(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Suv'
        print(f"This is {self.car_type} car.")


class Truck(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = 'Truck'
        print(f"This is {self.car_type} car.")


class FactoryClass:

    def create_instance(self, brand, model, car_type):
        if car_type == 'Sedan':
            return Sedan(brand, model)
        if car_type == 'Suv':
            return Suv(brand, model)
        if car_type == 'Truck':
            return Truck(brand, model)


fc = FactoryClass()
print(fc.create_instance('Toyota', 'cramy', 'Sedan'))
print(fc.create_instance('Ford', 'Explorer', 'Suv'))
print(fc.create_instance('Chevrolet', 'Silverado', 'Truck'))
