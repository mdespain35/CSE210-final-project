import arcade
from game import constants

# The almighty bullet, destroyer of all, aliens, barriers, or ships. None survive the wrath of the bullet


class Bullet(arcade.Sprite):
    def __init__(self, player: arcade.Sprite):
        filepath = constants.BULLET_SPRITE
        super().__init__(filepath, constants.BULLET_SCALING)
        # TODO: Set dy value of velocity equal to the bullet speed constant multiplied by direction
        self.change_y = constants.BULLET_SPEED
        # Set point values equal to the passed x and y respectively
        self.center_x = player.center_x
        self.center_y = player.center_y

    def update(self):
        super().update()
        # If bullet goes off screen. Kill it.
        if(self.top > constants.SCREEN_HEIGHT + self.height):
            self.remove_from_sprite_lists()
