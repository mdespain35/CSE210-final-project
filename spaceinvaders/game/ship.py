import arcade
from game import constants
from game.bullet import Bullet

# Our main character and protagonist, the ship!


class Ship(arcade.Sprite):
    def __init__(self):
        filename = constants.SHIP_SPRITE
        super().__init__(filename, constants.SHIP_SCALING)
        # TODO: Set starting point of the ship as the middle of the screen, set ship's radius
        self.center_x = constants.SCREEN_WIDTH / 2
        self.center_y = self.bottom + (self.height + 5)

    def key_press(self, key):
        # When/if key is pressed, move sprite left or right
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = constants.SHIP_THRUST * -1
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = constants.SHIP_THRUST

    def key_release(self, key):
        # Set the current position to stop when key is released
        self.change_x = 0

    def update(self):
        super().update()
        # Check for boundaries so that the ship does not go outside of them
        if self.left < 0:
            self.left = 0
        elif self.right > constants.SCREEN_WIDTH - 1:
            self.right = constants.SCREEN_WIDTH - 1
