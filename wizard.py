import pygame

class Wizard:
  def __init__(self, screen):
      self.screen = screen
      self.image = pygame.image.load('images/wizards/wizardFirstRoom.png')
      self.image = pygame.transform.scale(self.image, (65, 78))
      self.screen_rect = screen.get_rect()
      self.rect = self.image.get_rect()

      self.rect.centery = 560
      self.rect.centerx = 575


  def blitme(self):
      self.screen.blit(self.image, self.rect)

  def update(self, game_settings):
      pass