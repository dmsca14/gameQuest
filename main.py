# Code created by: Chris Bradfield
    # Edited by Dominic Sangster

# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 2
# Video link: https://www.youtube.com/watch?v=8LRI0RLKyt0
# Player movement
# © 2019 KidsCanCode LLC / All rights reserved.

import pygame as pg
import random
from pygame.sprite import Sprite
from sprites import *

# game options/settings
TITLE = "Hopper!"
WIDTH = 480
HEIGHT = 600
FPS = 60