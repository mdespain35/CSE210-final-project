import arcade
import constants
import random
# The space invaders themselves

class Alien(arcade.Sprite):
    def __init__(self, x, y):
        filename = constants.ALIEN_SPRITE
        super().__init__(filename, constants.SCALING)
        # TODO: Set velocity equal to alien speed constant, set center values equal to x, y values passed
        self.time_between_firing = random.randint(1, 3)

        self.center_x = x
        self.center_y = y 
        self.enemy_list = arcade.SpriteList()

        self.enemy = arcade.Sprite(filename, constants.SCALING)
        self.enemy.velocity = (constants.ALIEN_SPEED, 0) 

    def advance(self):
        # TODO: Advance aliens along screen, once they hit the edge of screen, move them down and reverse dx value from velocity

        if self.enemy.right in self.enemy_list == 0:
            for enemy in self.enemy_list:

                enemy.change_y = enemy.change_y - 1
                enemy.reverse(self.enemy.change_x)

    def fire_bullet(self):
        # TODO: Have each alien have a small chance of firing a bullet every 3 seconds
        # Wait to implement this until bullets have been implemented. 
        pass