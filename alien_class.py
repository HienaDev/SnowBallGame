import pygame, sys
import pygame.freetype
import random
from aliens_variable import *
from gamedata import *
import math



class RayShot:

    def __init__(self):

        self.pos = [0, 0]
        self.a = 0

class Player:

    shots10 = []
    shots11 = []
    shots20 = []
    shots21 = []
    shots30 = []
    shots31 = []
    shots40 = []
    shots41 = []
    shots50 = []
    shots51 = []

    #eeps track of hot air particles
    shots = [shots10, shots11, shots20, shots21, shots30, shots31, shots40, shots41, shots50, shots51]

    active_lanes = [0, 0, 0, 0, 0]

    def __init__(self):
        
        self.image = pygame.transform.scale(pygame.image.load("alien_char.png"), (80, 110))
        self.pos = [-10, 20]
        self.shooting = 0
        self.a = 0
        self.lane = 1

    def shoot_air(self, lane):

        
        if (lane == 1):

            self.shooting_air((40, 15), 0)
            self.shooting_air((40, 45), 1)

        if (lane == 2):

            self.shooting_air((40, 145), 2)
            self.shooting_air((40, 175), 3)

        if (lane == 3):

            self.shooting_air((40, 275), 4)
            self.shooting_air((40, 305), 5)

        if (lane == 4):

            self.shooting_air((40, 405), 6)
            self.shooting_air((40, 435), 7)

        if (lane == 5):

            self.shooting_air((40, 535), 8)
            self.shooting_air((40, 565), 9)

    def shooting_air(self, pos, shot):
        
        self.a += 3.4
        self.shots[shot].append(RayShot())

        self.shots[shot][len(self.shots[shot]) - 1].a = self.a

        if len(self.shots[shot]) > 1:
            
            self.shots[shot][len(self.shots[shot]) - 1].pos = [self.shots[shot][len(self.shots[shot]) - 2].pos[0] + 5, pos[1] + 50]
            
        else:

            self.shots[shot][len(self.shots[shot]) - 1].pos = [pos[0] + 80, pos[1] + 50]

        if (len(self.shots[shot]) > 10):

            del self.shots[shot][0]


    def delete_ray(self, lane):
        
        if (lane == 1):

            self.shots[0] = []
            self.shots[1] = []

        if (lane == 2):

            self.shots[2] = []
            self.shots[3] = []

        if (lane == 3):

            self.shots[4] = []
            self.shots[5] = []

        if (lane == 4):

            self.shots[6] = []
            self.shots[7] = []

        if (lane == 5):

            self.shots[8] = []
            self.shots[9] = []



PLAYER = Player()