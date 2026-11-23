import pygame

class MagicWizard:
  def __init__(self, screen):
      self.screen = screen
      self.image = pygame.image.load('images/wizards/wizardSecondRoom.png')
      self.image = pygame.transform.scale(self.image, (52, 78))
      self.screen_rect = screen.get_rect()
      self.rect = self.image.get_rect()

      self.rect.centery = 400
      self.rect.centerx = 310


  def blitme(self):
      self.screen.blit(self.image, self.rect)

  def update(self, game_settings):
      pass