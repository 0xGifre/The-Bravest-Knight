"""Replacement second-room NPC using an existing project sprite."""
from wizard import Wizard


class MagicWizard(Wizard):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.center = (307, 405)
