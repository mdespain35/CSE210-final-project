from game.ship import Ship
from game.bullet import Bullet
from game.alien import Alien
import arcade
from game import constants
import random


class Director(arcade.Window):

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        # Loads sound
        self.ship_bullet_sound = arcade.load_sound(constants.SHIP_SOUND)

        # self.held_keys = set()

    def setup(self):
        # Sets up the game and initializes the variables
        self.all_sprites = arcade.SpriteList()
        self.bullet_sprite = arcade.SpriteList()
        self.alien_bullet_sprite = arcade.SpriteList()
        self.enemy_sprite = arcade.SpriteList()
        #Variable for spawning the alien
        alien_spawn_x = 100

        self.ship = Ship()

        self.all_sprites.append(self.ship)
        
        while alien_spawn_x <= 800:

            self.alien = Alien(alien_spawn_x)
            alien_spawn_x += 200
            self.enemy_sprite.append(self.alien)

    def on_draw(self):
        """
        Called automatically  by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: Draw each object
        # Use Sprite Lists
        self.bullet_sprite.draw()
        self.alien_bullet_sprite.draw()
        self.all_sprites.draw()
        self.enemy_sprite.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        # self.check_keys()
        self.enemy_sprite.update()
        self.all_sprites.update()
        self.bullet_sprite.update()
        self.fire_bullet()
        # TODO: Tell everything to advance or move forward one step in time

        # TODO: Check for collisions
        self.check_collisions()

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        Performing various functions depending on the key pressed.
        """
        # Modified all keys so user can use AD or directional keys

        # TODO: Implement what these keys do when pressed
        pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """

        # TODO: Implement ship class so this makes sense
        self.ship.key_press(key)

        if key == arcade.key.SPACE:
            arcade.play_sound(self.ship_bullet_sound)
            bullet = Bullet(self.ship)
            self.bullet_sprite.append(bullet)

        # self.held_keys.add(key)
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
        self.ship.key_release(key)
        # if key in self.held_keys:
        # self.held_keys.remove(key)

    def check_collisions(self):
        """
        Checks to see if alien bullets have hit the ship and if ship bullets have hit the aliens.
        Updates scores and removes dead items.
        :return:
        """
        # TODO: Implement collision logic
        # Checks if any of the alien bullets collide with the ship and remove the ship if so
        for abullet in self.alien_bullet_sprite:
            if(arcade.check_for_collision(self.all_sprites[0], abullet)):
                self.all_sprites.clear()

        # Checks if the ships bullets hit any of the aliens
        for bullet in self.bullet_sprite:
            for alien in self.enemy_sprite:
                if (arcade.check_for_collision(bullet, alien)):
                    self.enemy_sprite.remove(alien)
                    self.bullet_sprite.remove(bullet)

        


    def fire_bullet(self):
        # TODO: Have each alien have a small chance of firing a bullet every 3 seconds
        # Wait to implement this until bullets have been implemented. 
        for alien in self.enemy_sprite:
            random_chance_of_firing = random.randint(1,100)

            if random_chance_of_firing == 10:
                arcade.play_sound(self.ship_bullet_sound)
                bullet = Bullet(alien)
                bullet.change_y = -1 * bullet.change_y
                bullet.angle = 180
                self.alien_bullet_sprite.append(bullet)

# TODO: Move this into the appropriate file to have it run once everything has been implemented.
"""
Logic needed to actually start game:
    window = Director(800, 600)
    arcade.run()
"""

