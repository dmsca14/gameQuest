# © 2019 KidsCanCode LLC / All rights reserved.
# Hopper!
# Edited by: Dominic Sangster

import pygame as pg
from threading import *
import time
from settings import *
from pygame.sprite import Group
# from pg.sprite import Group
import random
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = Group()
        self.platforms = Group()
        # self.monsters = Group()
        self.platcount = 0
        self.projectiles = Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        ground = Platform(0, HEIGHT-40, WIDTH, 40)
        # plat1 = Platform(200, 400, 150, 20)
        # plat2 = Platform(150, 300, 150, 20)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        print(*self.platforms)
        self.tempGroup = Group()
        # self.all_sprites.add(plat1)
        # self.platforms.add(plat1)
        # self.all_sprites.add(plat2)
        # self.platforms.add(plat2)

        # generates platforms that don't touch each other...
        # cite sources...wwwad a
        for plat in range(0, 10):
            if len(self.platforms) < 2:
                plat = Platform(random.randint(0,WIDTH-100), random.randint(0,HEIGHT-100), 100, 15)
                self.platforms.add(plat)
                self.all_sprites.add(plat)
                # print(self.platforms)
            # break
            while True:
                newPlat = Platform(random.randint(0,WIDTH-100), random.randint(0,HEIGHT-100), 100, 15)
                self.tempGroup.add(newPlat)
                selfCollide = pg.sprite.groupcollide(self.tempGroup, self.platforms, True, False)
                allCollide = pg.sprite.groupcollide(self.tempGroup, self.all_sprites, True, False)
                if not selfCollide and not allCollide:
                    self.platforms.add(newPlat)
                    self.all_sprites.add(newPlat)
                    self.tempGroup.remove(newPlat)
                    # print(len(self.tempGroup))
                    break
        # for monster in range(0,5):
        #     for plat in self.platforms:
        #         monster = Monster(self)
        #         monster.pos.y = plat.rect.y
        #         monster.pos.x = plat.rect.x
        #         self.monsters.add(monster)
        #         self.all_sprites.add(monster)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # # Update - listen to see if anything changes...
        self.all_sprites.update()
        # for p in self.projectiles:s
        #     # print(p.birth)
        # if p.rect.y < 0:
        #     p.kill()
        # # print(self.projectiles)
        # phits = pg.sprite.groupcollide(self.projectiles, self.platforms, True, True)
        # if phits:
        #     print("a projectile collided with a plat...")
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            if self.player.rect.top > hits[0].rect.top:
                # print("i hit my head")
                self.player.vel.y = 15
                self.player.rect.top = hits[0].rect.bottom + 5
            else:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top+1
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    print(len(self.platforms))
        # if player approaches terminal velocity
        # TERMINAL_VEL variable is defined in settings
        # SUCCESS!
        if self.player.vel.y > TERMINAL_VEL:
            self.player.vel.y = TERMINAL_VEL

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
pg.quit()