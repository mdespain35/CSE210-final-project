import arcade
from game import constants
import random
from game.bullet import Bullet
# The space invaders themselves

class Alien(arcade.Sprite):
    def __init__(self):
        filename = constants.ALIEN_SPRITE
        super().__init__(filename, constants.ALIEN_SCALING)
        # TODO: Set velocity equal to alien speed constant, set center values equal to x, y values passed
        self.change_x = constants.ALIEN_SPEED
        self.center_x = constants.SCREEN_WIDTH / 2
        self.center_y = constants.SCREEN_HEIGHT

    def advance(self):
        # TODO: Advance aliens along screen, once they hit the edge of screen, move them down and reverse dx value from velocity
        if self.left == 0 or self.right == constants.SCREEN_WIDTH:

            self.center_y = self.center_y - 10
            self.change_x = self.change_x * -1

    # def fire_bullet(self,):
    #     # TODO: Have each alien have a small chance of firing a bullet every 3 seconds
    #     # Wait to implement this until bullets have been implemented. 
    #     random_chance_of_firing = random.randint(1,10)

    #     if random_chance_of_firing == 10:
    #         arcade.play_sound(self.bullet_fire)
    #         self.bullet