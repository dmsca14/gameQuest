# This code was created by: Dominic Sangster

# import modules
from finalSettings import *
from finalSprites import *
import pygame as pg
from pygame.sprite import Sprite
import random
from os import path

# instantiate the game as a class
class Game():
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = Group()
        self.player = Player(self)
        self.orb = Orb(self)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.orb)

    def update(self):
        # collision
        score = 0
        hits = pygame.sprite.spritecollide(self.player, self.orb, True)
            if hits:
                self.orb.kill()
                score += 1
                print(score)

            



# woooooooooooooo

