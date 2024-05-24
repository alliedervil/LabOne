#This code was written with the help of chatGPT 

class AlienBase:
    def __init__(self, position, health):
        self.position = position
        self.health = health
        print(f"AlienBase initialized at position {position} with health {health}")

    def spawn(self, new_position):
        self.position = new_position
        self.health = 100
        print(f"Alien spawned at position {new_position} with health {self.health}")

    def takeDamage(self, damage):
        self.health -= damage
        print(f"Alien took {damage} damage, health now {self.health}")
        if self.health <= 0:
            print("Alien destroyed")
