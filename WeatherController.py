#This code was written with the help of chatGPT 

class WeatherController:
    def __init__(self):
        self.currentWeather = None
        self.weatherConditions = []
        print("WeatherController initialized with no current weather and empty weather conditions")

    def updateWeather(self, weather):
        self.currentWeather = weather
        print(f"Weather updated to {weather}")

    def applyWeatherEffects(self):
        for condition in self.weatherConditions:
            condition.applyEffect()
        print("Applied all weather effects")

    def removeWeatherEffects(self):
        for condition in self.weatherConditions:
            condition.removeEffect()
        print("Removed all weather effects")
