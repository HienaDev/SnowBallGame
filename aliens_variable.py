
import pygame, sys
import pygame.freetype
import math

#Initializing a bunch of colors to use in the game                                                                 

white = (240, 240, 240)
black = (10, 10, 10)
background_black = (13, 11, 11)
red = (240, 10, 10)
pink = (240, 126, 126)
blue = (10, 10, 205)
darkblue = (10, 10, 100)
yellow = (240, 240, 10)
babypink = (240, 180, 180)
grey = (105, 105, 105)
brown = (89,59,19)
babyblue = (135,206,250)

#Images

vent = pygame.image.load("vent.png")
platform = pygame.image.load("platform.png")
glass = pygame.image.load("glass.png")
star_background = pygame.image.load("star_background.png")


#Resolution

res = (800, 665)

#Lanes

lane1 = [800, 85]
lane2 = [800, 215]
lane3 = [800, 345]
lane4 = [800, 475]
lane5 = [800, 605]
exit_lane = [800, 800]

lanes = [lane1, lane2, lane3, lane4, lane5, exit_lane]

#Function to calculate rotational matrix
def calculate_r_matrix(ang):

    ang = math.radians(ang)
    return ([[math.cos(ang), -math.sin(ang)], [math.sin(ang), math.cos(ang)]])