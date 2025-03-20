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

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()
