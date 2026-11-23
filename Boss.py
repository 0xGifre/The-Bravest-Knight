import pygame
import random

class BossEnemy():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/boss/boss.png')
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = (304, 368)

    def blitme(self):
      self.screen.blit(self.image, self.rect)


    def update(self):
        pass
   #    self.attack_timer += 1
    #    if self.attack_timer >= 300:  # Ворог бос атакує кожні 300 кадрів (приблизно 5 секунд)
          #  self.attack()
          #  self.attack_timer =0




