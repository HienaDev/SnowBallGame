import pygame, sys
import pygame.freetype
import random
from aliens_variable import *
from alien_class import *
import numpy as np

snowballs = []

class Balls:

    def __init__(self):
        
        self.pos = []
        self.lane = 0
        self.scale = 100
        self.speed = [-1.5, 0]
        self.rotation = 0
        self.melting = 0
        self.image = pygame.transform.scale(pygame.image.load("snowball.png"), (100, 100))

class BallFunctions:


    def create_ball(self, lane):

        snowballs.append(Balls())
        snowballs[len(snowballs) - 1].lane = lane
        snowballs[len(snowballs) - 1].pos = lanes[lane - 1]

    def update_balls(self):

        pos = 0
        removePos = -1

        for ball in snowballs:
            
            #if ball.speed == [-2, 0]:
            ball.rotation += 1
                
            ball.pos = np.add(ball.pos, ball.speed)
            rotimage = pygame.transform.rotate(ball.image, ball.rotation)
            rect = rotimage.get_rect(center = ball.pos)
            GAMEDATA.screen.blit(rotimage, rect)

            

            if ball.melting == 1:

                ball.speed = [-1, 0]
                        
                if ball.scale <= 0.5:

                    removePos = pos
                else:

                    ball.scale -= 0.5
                    ball.pos = np.add(ball.pos, [0, 0.25])
                    ball.image = pygame.transform.scale(pygame.image.load("snowball.png"), (ball.scale, ball.scale))

            for shot in PLAYER.shots:
            
                for ray in shot:

                    if (ray.pos[0] >= ball.pos[0] and PLAYER.active_lanes[ball.lane - 1] == 1 and
                        ray.pos[1] > lanes[ball.lane -1][1] and ray.pos[1] < lanes[ball.lane][1]):
                        
                        ball.melting = 1

                        PLAYER.active_lanes[ball.lane - 1] = 0

                    


            pos += 1

        if removePos != -1:

            del snowballs[removePos]
            
        

        





BALLS = BallFunctions()
BALL = Balls()