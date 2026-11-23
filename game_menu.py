import os, pygame, sys
from pygame.locals import *



class Game_menu():
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.bg_image = pygame.image.load('images/menu_bg.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (800, 650)).convert()
        self.bg_button = pygame.image.load('images/button_bg.png')
        self.bg_button_rect = self.bg_button.get_rect()
        self.bg_button = pygame.transform.scale(self.bg_button, (385, 50)).convert_alpha()

        self.size = screen.get_size()
        self.width = self.size[0]
        self.height = self.size[1]

        self.title = pygame.Rect(
            ((self.width / 16) + 1, (self.height / 8) + 1, 7 * self.width / 8, self.height / 4))
        self.start_menu_but1 = pygame.Rect(
            ((self.width / 4) + 1, (self.height / 2) + 1, 2 * self.width / 4, self.height / 10))
        self.start_menu_but2 = pygame.Rect(((self.width / 4) + 1, (self.height / 2) + 1 + (3 * self.height / 20),
                                       2 * self.width / 4, self.height / 10))
        self.start_menu_but3 = pygame.Rect(((self.width / 4) + 1, (self.height / 2) + 1 + (6 * self.height / 20),
                                       2 * self.width / 4, self.height / 10))


        # Draws dark blue rectangles.
       # pygame.draw.rect(screen, (0, 0, 150), self.menu1)
       # pygame.draw.rect(screen, (0, 0, 150), self.menu2)
       # pygame.draw.rect(screen, (0, 0, 150), self.menu3)

        # Draws blue ovals on top of the rectangles.
       # pygame.draw.ellipse(screen, (0, 0, 150), self.title)
       # pygame.draw.ellipse(screen, (0, 0, 255), self.menu1)
       # pygame.draw.ellipse(screen, (0, 0, 255), self.menu2)
       # pygame.draw.ellipse(screen, (0, 0, 255), self.menu3)

        # pygame.font.Font takes in a font name and an integer for its size.
        # Free Sans Bold comes with Pygame (Sweigart 2012 p. 30).
        self.font_title = pygame.font.Font(None, 64)
        self.font_menu = pygame.font.Font(None, 32)

        # Creates and draws the text.
        self.surface_title = self.font_title.render('The Bravest Knight', True, (139, 69, 19))
        self.rect_title = self.surface_title.get_rect()  # get_rect() transfer to rectangle
        self.rect_title.center = (self.width / 2, (self.height / 4) + 1)

        self.surface_start_game = self.font_menu.render('START GAME', True, (0, 0, 0))
        self.rect_start_game = self.surface_start_game.get_rect()
        self.rect_start_game.center = (self.width / 2.05, (self.height / 2) + (self.height / 25) + 3)

        self.surface_options = self.font_menu.render('GAME OPTIONS', True, (0, 0, 0))
        self.rect_options = self.surface_options.get_rect()
        self.rect_options.center = (self.width / 2.05, (self.height / 2) + (4 * self.height / 21) + 3)

        self.surface_exit = self.font_menu.render('EXIT', True, (0, 0, 0))
        self.rect_exit = self.surface_exit.get_rect()
        self.rect_exit.center = (self.width / 2.05, (self.height / 2) + (7 * self.height / 20.5) + 3)

    def draw_menu(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.surface_title, self.rect_title)
        self.screen.blit(self.bg_button, (self.width / 5.75, (self.height / 2) + 5))
        self.screen.blit(self.bg_button, (self.width / 5.75, (self.height / 1.55) + 10))
        self.screen.blit(self.bg_button, (self.width / 5.75, (self.height / 1.25) + 5))
        self.screen.blit(self.surface_start_game, self.rect_start_game)
        self.screen.blit(self.surface_options, self.rect_options)
        self.screen.blit(self.surface_exit, self.rect_exit)

        #print(self.rect_start_game)
        #print(self.rect_options)
        #print(self.rect_exit)