import arcade
import constants

# The almighty bullet, destroyer of all, aliens, barriers, or ships. None survive the wrath of the bullet

class Bullet(arcade.Sprite):
    def __init__(self, x, y, direction):
        filepath = constants.BULLET_SPRITE
        super().__init__(filepath, constants.SCALING)
        # TODO: Set dy value of velocity equal to the bullet speed constant multiplied by direction
        self.dy = constants.BULLET_SPEED * direction
        # Set point values equal to the passed x and y respectively
        self.bx = x
        self.by = y


    def draw_self(self):
        # TODO: Implement initial drawing of bullet using arcade package
        pass

    def advance(self):
        # TODO: Add dy value of velocity to y value of center, check if bullet goes off screen.
        self.velocity = (0 , self.dy)
        # If bullet goes off screen. Kill it.
        if(self.top > 600 or self.bottom < 0):
            self.remove_from_sprite_lists()
        pass