"""Explicit replacements for assets missing from the supplied project."""
from pathlib import Path
import pygame


def load_plot(path, room):
    if Path(path).is_file():
        return pygame.image.load(path).convert_alpha()
    panel = pygame.Surface((608, 370), pygame.SRCALPHA)
    panel.fill((23, 25, 35, 245))
    font = pygame.font.Font(None, 28)
    lines = [
        'Traveller’s advice',
        '',
        'Move with WASD or the arrow keys.',
        'Space: shoot. R: reload. Esc: pause.',
        'Find the passage at the upper left.' if room == 1
        else 'Find the passage at the top of the central aisle.',
    ]
    for index, line in enumerate(lines):
        panel.blit(font.render(line, True, (240, 235, 220)), (20, 25 + index * 36))
    pygame.draw.rect(panel, (155, 115, 55), (413, 309, 156, 40), border_radius=6)
    panel.blit(font.render('Continue', True, (255, 255, 255)), (447, 318))
    return panel
