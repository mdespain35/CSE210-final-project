import os
# Constants to be used throughtout the game
SHIP_SCALING = 0.8
BULLET_SCALING = 0.05

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 8
BULLET_RADIUS = 20

ALIEN_SPEED = 2
ALIEN_RADIUS = 10

SHIP_THRUST = 3
SHIP_RADIUS = 30

BARRIER_RADIUS = 5

PATH = os.path.dirname(os.path.abspath(__file__))
SHIP_SPRITE = PATH + "/images/ship.png"
BULLET_SPRITE = PATH + "/images/bullet.png"
SHIP_SOUND = PATH + "/sounds/ship_bullet_sound.mp3"