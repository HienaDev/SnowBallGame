import pygame, sys
import pygame.freetype
from aliens_variable import *


class GameData:
    
    score = 0
    lives = 3
    boats_destroyed = 0

    #Starts the game screen with selected resolution
    def start_up(self, resolution):

        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        self.res = resolution

    def change_window_name(self, name):

        pygame.display.set_caption(name) # Changes the name of the window

    def draw_map(self):

        #Background
        self.screen.blit(star_background, (0, 0))

        #Platforms
        self.screen.blit(pygame.transform.scale(platform, (800, 20)), (0, -7))
        self.screen.blit(platform, (0, 130))
        self.screen.blit(platform, (0, 260))
        self.screen.blit(platform, (0, 390))
        self.screen.blit(platform, (0, 520))
        self.screen.blit(platform, (0, 650))

        #Ventilation
        self.screen.blit(vent, (75, 15))
        self.screen.blit(vent, (75, 145))
        self.screen.blit(vent, (75, 275))
        self.screen.blit(vent, (75, 405))
        self.screen.blit(vent, (75, 535))

    def draw_glass(self):

        #Glass
        self.screen.blit(glass, (115, 15))
        self.screen.blit(glass, (115, 145))
        self.screen.blit(glass, (115, 275))
        self.screen.blit(glass, (115, 405))
        self.screen.blit(glass, (115, 535))

    def draw_buttons(self):
        
        pygame.draw.rect(self.screen, red, (60, 60, 15, 30))
        pygame.draw.rect(self.screen, red, (60, 190, 15, 30))
        pygame.draw.rect(self.screen, red, (60, 320, 15, 30))
        pygame.draw.rect(self.screen, red, (60, 450, 15, 30))
        pygame.draw.rect(self.screen, red, (60, 580, 15, 30))

    def draw_active_buttons(self, active_lanes):

        pygame.draw.rect(self.screen, background_black, (60, 60, 10 * active_lanes[0], 30))
        pygame.draw.rect(self.screen, background_black, (60, 190, 10 * active_lanes[1], 30))
        pygame.draw.rect(self.screen, background_black, (60, 320, 10 * active_lanes[2], 30))
        pygame.draw.rect(self.screen, background_black, (60, 450, 10 * active_lanes[3], 30))
        pygame.draw.rect(self.screen, background_black, (60, 580, 10 * active_lanes[4], 30))

    # This function fills the screen with a color
    def clear(self, color):

        self.screen.fill(color)

    # This function updates the display
    def update(self):

        pygame.display.update()

GAMEDATA = GameData()