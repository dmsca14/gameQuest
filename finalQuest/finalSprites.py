from pygame.sprite import Sprite
import pygame as pg
import random
from os import path
from finalSettings import *

class Player(Sprite):
    # include game parameter to pass game class as argument in main...
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        # player look
        self.image = pg.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # position and movement properties
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.pos.x = WIDTH / 2
        self.pos.y = HEIGHT / 2
        self.vel.x = 0
        self.vel.y = 0
        self.acc.x = 5
        self.acc.y = 5

    def draw(self, surface):
       surface.blit(self.image, (self.x, self.y))

    def update(self):
        #check to see if player state changes
        self.acc.x = 5
        self.acc.y = 5
        keys = pg.key.get_pressed()
        # player moves when keys get pressed
        if keys[pg.K_a]:
            self.vel.x -= self.acc.x
            self.pos.x += self.vel.x
        if keys[pg.K_d]:
            self.vel.x += self.acc.x
            self.pos.x += self.vel.x
        if keys[pg.K_w]:
            self.vel.y += self.acc.y
            self.pos.y += self.vel.y
        if keys[pg.K_s]:
            self.vel.y -= self.acc.y
            self.pos.y += self.vel.y
        # terminal velocity
        if self.vel.x > vxmax:
            self.vel.x = vxmax
        if self.vel.y > vymax:
            self.vel.y = vymax
        
    # movement stuff
        # friction
        self.acc += self.vel.x * friction
        self.acc.y += self.vel.y * friction
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # screen keeps player inside, no wrapping around the sides
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT

class Orb(Sprite):
    def __init__(self):
        # orb look
        self.image = pg.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

        # orb position and movement properties
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.pos.x = WIDTH / (random.randint(1,8))
        self.pos.y = HEIGHT / (random.randint(1,8))
        self.vel.x = 0
        self.vel.y = 0
        self.acc.x = 0
        self.acc.y = 0

    def draw(self, surface):
       surface.blit(self.image, (self.x, self.y))
        
    def update(self):