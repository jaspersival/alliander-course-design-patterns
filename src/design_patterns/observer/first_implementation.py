class CurrentConditionsDisplay:
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


class StatisticsDisplay:
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


class ForecastDisplay:
    def update(self, temperature: float, humidity: float, pressure: float):
        pass


# Taking a first, misguided implementation of the Weather Station
class WeatherData:
    def __init__(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def measurements_changed(self):
        # This method is called whenever the weather measurements have been updated
        CurrentConditionsDisplay.update(self.temperature, self.humidity, self.pressure)
        StatisticsDisplay.update(self.temperature, self.humidity, self.pressure)
        ForecastDisplay.update(self.temperature, self.humidity, self.pressure)

    # Other WeatherData methods here
