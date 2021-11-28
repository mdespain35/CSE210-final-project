from ship import Ship
import arcade
import constants


class Director(arcade.Window):

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.ship = Ship()

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: Draw each object
        self.ship.draw_self()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        self.ship.advance()

        # TODO: Check for collisions

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        Performing various functions depending on the key pressed.
        """
        # Modified all keys so user can use AD or directional keys

        # TODO: Implement what these keys do when pressed

        if arcade.key.LEFT in self.held_keys or arcade.key.A in self.held_keys:
            self.ship.move_left()

        if arcade.key.RIGHT in self.held_keys or arcade.key.D in self.held_keys:
            self.ship.move_right()

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """

        # TODO: Implement ship class so this makes sense
        self.held_keys.add(key)
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                pass
        """

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

    def check_collisions(self):
        """
        Checks to see if bullets have hit asteroids and if asteroids have hit the ship.
        Updates scores and removes dead items.
        :return:
        """
        # TODO: Implement collision logic
        pass

    def clean_up_zombies(self):
        """
        Loops through arrays and removes any objects that have died.
        """

        # TODO: Implement clean up logic
        pass


# TODO: Move this into the appropriate file to have it run once everything has been implemented.
"""
Logic needed to actually start game:
    window = Director(800, 600)
    arcade.run()
"""

window = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
arcade.run()
