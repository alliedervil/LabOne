#This code was written with the help of chatGPT 

class Clock:
    def __init__(self):
        self.currentTime = 0
        print("Clock initialized with currentTime set to 0")

    def tick(self):
        self.currentTime += 1
        print(f"Clock ticked, currentTime: {self.currentTime}")

    def reset(self):
        self.currentTime = 0
        print("Clock reset to 0")
