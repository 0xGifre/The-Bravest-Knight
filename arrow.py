import pygame
from pygame.sprite import Sprite


class Arrow(Sprite):
    def __init__(self, screen, settings, main_hero):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/fireball/fireballDown.png')
        self.image = pygame.transform.scale(self.image,(14, 18)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = main_hero.rect.centerx - 2
        self.rect.centery = main_hero.rect.centery + 7

        if main_hero.last_position == 2 or main_hero.last_position == 4:
            if main_hero.last_position == 2:
                self.image = pygame.image.load('images/fireball/fireballUp.png')
            else:
                self.image = pygame.image.load('images/fireball/fireballDown.png')
            self.image = pygame.transform.scale(self.image, (9, 13)).convert_alpha()
            self.y_direction = -2 if main_hero.last_position == 2 else 2
        else:
            self.y_direction = 0

        if main_hero.last_position == 1 or main_hero.last_position == 3:
            if main_hero.last_position == 1:
                self.image = pygame.image.load('images/fireball/fireballLeft.png')
            else:
                self.image = pygame.image.load('images/fireball/fireballRight.png')

            self.image = pygame.transform.scale(self.image, (13, 9)).convert_alpha()
            self.x_direction = -2 if main_hero.last_position == 1 else 2
        else:
            self.x_direction = 0

    def update(self):
        self.rect.y += self.settings.arrow_speed * self.y_direction
        self.rect.x += self.settings.arrow_speed * self.x_direction

    def draw_arrow(self):
        self.screen.blit(self.image, self.rect)