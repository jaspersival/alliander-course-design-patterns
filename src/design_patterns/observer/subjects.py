from abc import ABC, abstractmethod
from .observers import Observer


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer): ...

    @abstractmethod
    def remove_observer(self, observer: Observer): ...

    @abstractmethod
    def notify_observers(self): ...


class WeatherData(Subject):
    temperature: float
    humidity: float
    pressure: float

    def __init__(self):
        self.observers: list[Observer] = []

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def measurements_changed(self):
        """
        This method is here to keep the original interface in first_implementation.py intact.
        Other than that it is not needed to keep this method and the notify_observers method separate.
        """
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
