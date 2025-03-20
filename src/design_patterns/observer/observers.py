from abc import ABC, abstractmethod
import typing

if typing.TYPE_CHECKING:
    from .subjects import WeatherData


class Observer(ABC):
    @abstractmethod
    def update(self): ...


class CurrentConditionsDisplay(Observer):
    temperature: float
    humidity: float

    def __init__(self, weather_data: "WeatherData"):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.display()

    def display(self):
        print(
            f"Current conditions: {self.temperature}\u00b0C  and {self.humidity}% humidity"
        )


class StatisticsDisplay(Observer):
    max_temperature: float
    min_temperature: float
    avg_temperature: float

    def __init__(self, weather_data: "WeatherData"):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperatures: list[float] = []

    def update(self):
        self.temperatures.append(self.weather_data.temperature)
        self.max_temperature = max(self.temperatures)
        self.min_temperature = min(self.temperatures)
        self.avg_temperature = sum(self.temperatures) / len(self.temperatures)
        self.display()

    def display(self):
        print(
            f"Avg/Max/Min temperature: {self.avg_temperature}/{self.max_temperature}/{self.min_temperature}\u00b0C"
        )
