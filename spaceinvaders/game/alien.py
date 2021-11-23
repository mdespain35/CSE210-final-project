from moving_object import MovingObject
import constants

# The space invaders themselves

class Alien(MovingObject):
    def __init__(self, x, y):
        super().__init__()
        # TODO: Set velocity equal to alien speed constant, set center values equal to x, y values passed

    def draw_self(self):
        # TODO: Implement initial drawing of alien using arcade package
        pass

    def advance(self):
        # TODO: Advance aliens along screen, once they hit the edge of screen, move them down and reverse dx value from velocity
        pass

    def fire_bullet(self):
        # TODO: Have each alien have a small chance of firing a bullet every 3 seconds
        # Wait to implement this until bullets have been implemented. 
        pass