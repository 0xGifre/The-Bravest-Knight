import pygame
from pygame.sprite import Sprite

class Block(Sprite):
    def __init__(self, screen, block_size):
        super().__init__()
        self.screen = screen
        self.block_color = (255, 255, 255)
        self.block_size = block_size
        self.rect = pygame.Rect(self.block_size)

    def draw_block(self):
        pygame.draw.rect(self.screen, self.block_color, self.block_size)


