import pygame
import numpy as np
import math

def calculate_r_matrix(ang):

    ang = math.radians(ang)
    return ([[math.cos(ang), -math.sin(ang), 0], 
            [math.sin(ang), math.cos(ang), 0],
            [0, 0, 1]])

def calculate_s_matrix(scale):

    return([[scale, 0, 0], 
            [0, scale, 0],
            [0, 0, 1]])

snowball_image = (pygame.image.load("snowball.png"))

pygame.init()

pos = [100, 100, 1]

scale = 1000
ang = 0

screen = pygame.display.set_mode((800, 800))
while(True):

    screen.fill((0, 0, 0))
    screen.blit(snowball_image, (pos[0], pos[1]))

    if scale > 0.5:
        scale -= 1
    
    pos[0] += 0.1
    pos[1] -= 0.01

    pos[0] += 0.1
    ang += 1

    pygame.draw.line(screen, (250, 0, 0), (0, 100), (800, 100), 1)
    snowball_image = pygame.transform.scale(pygame.image.load("snowball.png"), (scale, scale))
    
    rotimage = pygame.transform.rotate(snowball_image, ang)
    rect = rotimage.get_rect(center = [pos[0], pos[1]])
    screen.blit(rotimage, rect)

    pygame.display.update()
