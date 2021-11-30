import os
# Constants to be used throughtout the game
SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 10
BULLET_RADIUS = 20

ALIEN_SPEED = 2
ALIEN_RADIUS = 10

SHIP_THRUST = 3
SHIP_RADIUS = 30

BARRIER_RADIUS = 5

PATH = os.path.dirname(os.path.abspath(__file__))
SHIP_SPRITE = PATH + "/images/ship.png"
