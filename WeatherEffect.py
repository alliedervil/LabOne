#This code was written with the help of chatGPT 

class WeatherEffect:
    def __init__(self, type, intensity):
        self.type = type
        self.intensity = intensity
        print(f"WeatherEffect created with type: {type} and intensity: {intensity}")

    def applyEffect(self):
        print(f"Applying weather effect of type: {self.type} with intensity: {self.intensity}")

    def removeEffect(self):
        print(f"Removing weather effect of type: {self.type}")
