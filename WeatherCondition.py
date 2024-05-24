#This code was written with the help of chatGPT 

class WeatherCondition:
    def __init__(self, type, intensity):
        self.type = type
        self.intensity = intensity
        print(f"WeatherCondition created with type: {type} and intensity: {intensity}")

    def applyCondition(self):
        print(f"Applying weather condition of type: {self.type} with intensity: {self.intensity}")
