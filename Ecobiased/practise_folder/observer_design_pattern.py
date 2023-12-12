# Observer Pattern Implementation for a Weather Station

from abc import ABC, abstractmethod


# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass


# Subject Interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# Concrete Observer (Display Device)
class DisplayDevice(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Display Device: Temperature={temperature}, Humidity={humidity}, Pressure={pressure}")


# Concrete Observer (Mobile App)
class MobileApp(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Mobile App: Weather Update - Temperature={temperature}, Humidity={humidity}")


# Concrete Subject (Weather Station)
class WeatherStation(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


# Usage Example
if __name__ == "__main__":
    # Create Weather Station
    weather_station = WeatherStation()

    # Create Observers (Display Device and Mobile App)
    display_device = DisplayDevice()
    mobile_app = MobileApp()

    # Register Observers with the Weather Station
    weather_station.register_observer(display_device)
    weather_station.register_observer(mobile_app)

    # Simulate Weather Updates
    weather_station.set_measurements(25, 60, 1015)
    weather_station.set_measurements(28, 65, 1020)
