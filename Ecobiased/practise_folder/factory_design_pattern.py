from abc import ABC, abstractmethod


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Sedan(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.car_type = "Sedan"
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

    def create_factory(self, car_type, brand, model):
        if car_type == 'Sedan':
            return Sedan(brand, model)
        if car_type == 'Suv':
            return Suv(brand, model)
        if car_type == 'Truck':
            return Truck(brand, model)
        else:
            return ValueError(f"Unknown car type: {car_type}")


fc = FactoryClass()
print(fc.create_factory('Sedan', 'Toyota', 'Camry'))
print(fc.create_factory('Suv', 'Ford', 'Explorer'))
print(fc.create_factory('Truck', 'Chevrolet', 'Silverado'))


class Car1(ABC):

    @abstractmethod
    def car_colour(self):
        pass


class Sedan1(Car1):

    def __init__(self, colour):
        self.colour = colour

    def car_colour(self):
        return f"The colour of this car is {self.colour}"


class Suv1(Car1):

    def __init__(self, colour):
        self.colour = colour

    def car_colour(self):
        return f"The colour of this car is {self.colour}"


class Truck1(Car1):

    def __init__(self, colour):
        self.colour = colour

    def car_colour(self):
        return f"The colour of this car is {self.colour}"


class FactoryClass1:

    def create_class1(self, car_type, car_colour):
        if car_type == "Suv":
            return Suv1(car_colour)
        if car_type == "Sedan":
            return Sedan1(car_colour)
        if car_type == "Truck":
            return Truck1(car_colour)
        else:
            return ValueError(f"Unknown car type.")


fc1 = FactoryClass1()
print(fc1.create_class1('Suv', 'blue'))
print(fc1.create_class1('Sedan', 'green'))
print(fc1.create_class1('Truck', 'Black'))





