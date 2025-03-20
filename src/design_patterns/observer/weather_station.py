from design_patterns.observer.subjects import WeatherData
from design_patterns.observer.observers import (
    CurrentConditionsDisplay,
    StatisticsDisplay,
)


def main():
    weather_data = WeatherData()
    CurrentConditionsDisplay(weather_data)
    StatisticsDisplay(weather_data)

    weather_data.set_measurements(30, 65, 30.4)
    weather_data.set_measurements(25, 70, 29.2)
    weather_data.set_measurements(20, 90, 29.2)


if __name__ == "__main__":
    main()
