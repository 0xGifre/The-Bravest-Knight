"""Replacement NPC; the original wizard module and art were not supplied."""
from pathlib import Path
import pygame


class Wizard:
    def __init__(self, screen):
        self.screen = screen
        path = Path(__file__).resolve().parent / 'images/NPC/Npc2/NpcL/NpcL1.png'
        self.image = pygame.transform.scale(pygame.image.load(str(path)).convert_alpha(), (45, 45))
        self.rect = self.image.get_rect(center=(550, 560))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
