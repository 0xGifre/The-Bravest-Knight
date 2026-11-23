import pygame


class Enemy():
    """A class to represent a single alien in the fleet."""

    def __init__(self, screen, settings):
        """Initialize the alien, and set its starting position."""
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()

        # Load the alien image, and set its rect attribute.
        self.image = pygame.image.load("images/npc/Npc1/NpcR/NpcR1.png")
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.rect.centery = self.screen_rect.centery - 245
        self.rect.centerx = self.screen_rect.centerx - 259


    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
