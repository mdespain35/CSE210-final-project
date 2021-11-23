# Basic class needed to move objects not controlled by player.

class Velocity:
    # Setting point to default, let the object modify it's position
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0