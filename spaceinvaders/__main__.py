from game import constants
from game.director import Director
import arcade

director = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
director.setup()

arcade.run()
