import arcade
import constants
# from spaceinvaders.game.constants import SHIP_RADIUS

# Our main character and protagonist, the ship!


class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__()
        # TODO: Set starting point of the ship as the middle of the screen, set ship's radius
        # self.center_x = constants.SCREEN_WIDTH / 2
        # self.center_y = constants.SCREEN_HEIGHT / 200
        self.x = constants.SCREEN_WIDTH / 2
        self.y = constants.SCREEN_HEIGHT / 20
        self.thruster = constants.SHIP_THRUST

    def draw_self(self):
        # TODO: Implement initial drawing of ship using arcade package
        arcade.draw_rectangle_filled(
            self.x, self.y, 60, 20, arcade.color.BLUE)

    def move_left(self):
        # TODO: Move ship left by the constant value of SHIP_THRUST
        self.thruster = -5
        self.x += self.thruster

    def move_right(self):
        # TODO: Move ship right by the constant value of SHIP_THRUST
        self.thuster = 5
        self.x -= self.thruster

    def advance(self):

        # self.x += self.thruster
        self.thruster = 0

    # def advance_left(self):
    #     self.x += self.thruster
    #     self.thruster = 0

    # def advance_right(self):
    #     self.x += self.thruster
    #     self.thruster = 0

    def fire_bullet(self):
        # TODO: Have the ship fire a bullet from its current position.
        # Wait to implement this until bullets have been implemented.
        pass
