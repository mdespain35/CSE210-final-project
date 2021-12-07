import arcade
import constants

# The almighty bullet, destroyer of all, aliens, barriers, or ships. None survive the wrath of the bullet

class Bullet(arcade.Sprite):
    def __init__(self, player:arcade.Sprite, direction):
        filepath = constants.BULLET_SPRITE
        super().__init__(filepath, constants.SCALING)
        # TODO: Set dy value of velocity equal to the bullet speed constant multiplied by direction
        self.change_y = constants.BULLET_SPEED * direction
        # Set point values equal to the passed x and y respectively
        self.center_x = player.center_x
        self.center_y = player.center_y


    def outOfBounds(self):
        # If bullet goes off screen. Kill it.
        if(self.top > 600 or self.bottom < 0):
            self.remove_from_sprite_lists()
        pass