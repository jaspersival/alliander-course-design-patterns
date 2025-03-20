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
