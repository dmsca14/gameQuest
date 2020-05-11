# This code was created by: Dominic Sangster
# import modules
import pygame as pg
# from sprites import *
import math
from finalSettings import *
from finalSprites import *

# instantiate the game as a class
class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

# instantiate player class
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        # self.image = pg.Surface((50,40))
        self.image = pg.transform.scale(player_img, (50, 40))
        # self.image = player_img
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = 10
        self.rect.bottom = 10
        self.speedx = 0
        self.speedy = 10

