import arcade
import constants

# Our main character and protagonist, the ship!

class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__()
        # TODO: Set starting point of the ship as the middle of the screen, set ship's radius

    def draw_self(self):
        # TODO: Implement initial drawing of ship using arcade package
        pass

    def move_left(self):
        # TODO: Move ship left by the constant value of SHIP_THRUST
        pass

    def move_right(self):
        # TODO: Move ship right by the constant value of SHIP_THRUST
        pass

    def fire_bullet(self):
        # TODO: Have the ship fire a bullet from its current position.
        # Wait to implement this until bullets have been implemented. 
        pass