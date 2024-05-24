# This was written with the help of chatGPT 

class Player:
    def __init__(self, initial_position=0):
        self.position = initial_position
        print(f"Player initialized at position {initial_position}")

    def move_left(self):
        if self.position > 0:
            self.position -= 1
            print(f"Player moved left to position {self.position}")

    def move_right(self, max_position):
        if self.position < max_position:
            self.position += 1
            print(f"Player moved right to position {self.position}")

    def get_position(self):
        return self.position
