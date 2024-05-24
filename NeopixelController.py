# This was written with the help of ChatGPT

from machine import Pin
import neopixel

class NeopixelController:
    def __init__(self, pin, num_leds):
        self.num_leds = num_leds
        self.np = neopixel.NeoPixel(Pin(pin), num_leds)
        print(f"NeopixelController initialized with {num_leds} LEDs on pin {pin}")

    def clear(self):
        print("Clearing all LEDs")
        for i in range(self.num_leds):
            self.np[i] = (0, 0, 0)
        self.np.write()

    def setPixel(self, index, color):
        if index >= 0 and index < self.num_leds:
            print(f"Setting LED at index {index} to color {color}")
            self.np[index] = color

    def show(self):
        print("Updating LEDs to show current state")
        self.np.write()
