import arcade
from game import constants
# The space invaders themselves

class Alien(arcade.Sprite):
    def __init__(self, x):
        filename = constants.ALIEN_SPRITE
        super().__init__(filename, constants.ALIEN_SCALING)
        # TODO: Set velocity equal to alien speed constant, set center values equal to x, y values passed
        self.change_x = constants.ALIEN_SPEED
        self.center_x = x
        self.center_y = constants.SCREEN_HEIGHT

    def update(self):
        super().update()
        # TODO: Advance aliens along screen, once they hit the edge of screen, move them down and reverse dx value from velocity
        if self.left == 0 or self.right == constants.SCREEN_WIDTH:

            self.center_y = self.center_y - 75
            self.change_x = self.change_x * -1
