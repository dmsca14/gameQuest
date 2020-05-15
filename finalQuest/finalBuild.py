# This code was created by: Dominic Sangster
# Derived from Mr. Cozort's class coding documents

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
        hits = pg.sprite.spritecollide(self.player, self.orb, False)
        if hits:
            self.orb.kill()
            score += 1
            print(score)
            self.all_sprites.add(self.orb)


# some pylint error is stopping pygame from initializing
'''i tracked it down to a settings.json file, but i have
no idea how to fix that problem in the .json file despite 
researching several online resources'''
# as such, I have not had a single opportunity to test run my final game
'''I was able to test snippets of it during development, and it mostly 
worked ok, but then the plyint thing broke and it all fell apart'''
        

