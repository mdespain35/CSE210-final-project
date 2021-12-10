import arcade
from game import constants
import random
# The space invaders themselves

class Alien(arcade.Sprite):
    def __init__(self):
        filename = constants.ALIEN_SPRITE
        super().__init__(filename, constants.SHIP_SCALING)
        # TODO: Set velocity equal to alien speed constant, set center values equal to x, y values passed
        self.chance_of_firing = random.randint(1, 3)
        self.change_x = constants.ALIEN_SPEED
        self.center_x = constants.SCREEN_WIDTH / 2
        self.center_y = 600

    def advance(self):
        # TODO: Advance aliens along screen, once they hit the edge of screen, move them down and reverse dx value from velocity
        if self.left == 0 or self.right == constants.SCREEN_WIDTH:

            self.center_y = self.center_y - 10
            self.reverse(self.change_x)

    def fire_bullet(self):
        # TODO: Have each alien have a small chance of firing a bullet every 3 seconds
        # Wait to implement this until bullets have been implemented. 
        pass