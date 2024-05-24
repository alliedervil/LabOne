# This was written with the help of chatGPT 

from machine import Pin, I2C
from lcd_display import LCDDisplay
from button import Button
from neopixel_controller import NeopixelController
import time

class GameController:
    def __init__(self):
        self.upDownCounter = 0
        self.highScore = 0
        self.weatherController = None
        self.lcdDisplay = LCDDisplay(sda=0, scl=1, i2cid=0)
        self.neopixelController = NeopixelController(pin=4, num_leds=30)
        self.joystick = None
        self.passiveBuzzer = None
        self.clock = None
        self.servoMotor = None
        self.stateModel = None
        self.buttons = [
            Button(pin=10, name="Button 1", buttonhandler=self),
            Button(pin=11, name="Button 2", buttonhandler=self),
            Button(pin=12, name="Button 3", buttonhandler=self),
            Button(pin=13, name="Button 4", buttonhandler=self)
        ]

    def startGame(self):
        print("Game Started")
        self.lcdDisplay.showText("Game Started", 0, 0)
        self.neopixelController.clear()
        self.updateScore(0)

    def updateScore(self, score):
        self.upDownCounter = score
        if score > self.highScore:
            self.highScore = score
        self.lcdDisplay.showText(f"Score: {score}", 1, 0)

    def buttonPressed(self, name):
        print(f"{name} pressed")
        if name == "Button 1":
            self.updateScore(self.upDownCounter + 1)
        elif name == "Button 2":
            self.updateScore(self.upDownCounter - 1)
        elif name == "Button 3":
            self.startGame()
        elif name == "Button 4":
            self.endGame()

    def buttonReleased(self, name):
        print(f"{name} released")

    def endGame(self):
        print("Game Ended")
        self.lcdDisplay.showText("Game Ended", 0, 0)
        self.neopixelController.clear()

# This part of the code initializes the GameController and starts the game
if __name__ == "__main__":
    game_controller = GameController()
    game_controller.startGame()

    while True:
        time.sleep(1)  # This simulates the game loop
