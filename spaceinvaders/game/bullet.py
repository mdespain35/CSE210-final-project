from moving_object import MovingObject
import constants

# The almighty bullet, destroyer of all, aliens, barriers, or ships. None survive the wrath of the bullet

class Bullet(MovingObject):
    def __init__(self, x, y, direction):
        super().__init__()
        # TODO: Set dy value of velocity equal to the bullet speed constant multiplied by direction
        # Set point values equal to the passed x and y respectively

    def draw_self(self):
        # TODO: Implement initial drawing of bullet using arcade package
        pass

    def advance(self):
        # TODO: Add dy value of velocity to y value of center, check if bullet goes off screen.
        # If bullet goes off screen. Kill it.
        pass