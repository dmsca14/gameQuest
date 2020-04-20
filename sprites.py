# Sprite classes for platform game
# © 2019 KidsCanCode LLC / All rights reserved.
# Edited by Dominic Sangster
# mr cozort planted a landmine by importing Sprite directly...

import pygame as pg
from threading import *
import time
from pygame.sprite import *
from settings import *
import math
vec = pg.math.Vector2

class Player(Sprite):
    # include game parameter to pass game class as argument in main...
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.hitpoints = 100
    def myMethod(self):
        pass
    
    def pew(self):
        laser = Pewpew(self.pos.x, self.pos.y, 10, 10)
        laser = Pewpew(self.game, self.pos.x + self.rect.width/2, self.pos.y, 10, 10)
        # print("trying to pewpewpew")
        self.game.all_sprites.add(laser)
        # self.game.platforms.add(laser)
        self.game.projectiles.add(laser)

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits: 
            self.vel.y = -15
    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_w]:
            self.pew()
            # self.acc.y = -PLAYER_ACC
        if keys[pg.K_s]:
            self.acc.y = PLAYER_ACC
        # ALERT - Mr. Cozort did this WAY differently than Mr. Bradfield...
        if keys[pg.K_SPACE]:
            self.jump()

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # self.acc.y += self.vel.y * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        # wrap vertically
        if self.pos.y < 0:
            self.kill
        if self.pos.y > HEIGHT-20 :
            self.pos.y = 20
        self.rect.midbottom = self.pos

# class Monster(Sprite):
#     # include game parameter to pass game class as argument in main...
#     def __init__(self, game):
#         Sprite.__init__(self)
#         self.game = game
#         self.image = pg.Surface((30, 40))
#         self.image.fill(LIGHTGREEN)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2, HEIGHT / 2)
#         self.pos = vec(WIDTH / 2, HEIGHT / 2)
#         self.vel = vec(0, 0)
#         self.acc = vec(0.5, 0)
#         self.hitpoints = 100        
#         self.rect.midbottom = self.pos

#     def update(self):
#         self.acc = vec(0, 0.5)
#         # apply friction
#         self.acc.x += self.vel.x * PLAYER_FRICTION
#         # self.acc.y += self.vel.y * PLAYER_FRICTION
#         # equations of motion
#         self.vel += self.acc
#         self.pos += self.vel + 0.5 * self.acc
#         # wrap around the sides of the screen
#         if self.pos.x > WIDTH:
#             self.pos.x = 0
#         if self.pos.x < 0:
#             self.pos.x = WIDTH
#         if self.pos.y < 0:
#             kill(self)
#         if self.pos.y > HEIGHT:
#             self.pos.y = 0
#         self.rect.midbottom = self.pos 

class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.image.fill(LIGHTBLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Pewpew(Sprite):
    def __init__(self, x, y, w, h):
        def __init__(self, game, x, y, w, h):
            Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((w, h))
        # self.image.fill(RED)
        self.image.fill(LIGHTBLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.birth = time.perf_counter_ns()
        self.lifespan = 1000000000

#     def update(self):
#         self.rect.y -= 5 
#         self.rect.y -= 5
#         self.now = time.perf_counter_ns()
#         if self.now - self.birth > self.lifespan:
#             self.kill() 

