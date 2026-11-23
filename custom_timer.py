import pygame


class Custom_timer():
    def __init__(self, screen, settings):
        self.settings = settings
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.screen = screen
        self.counter = 0
        self.size = screen.get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.font_title = pygame.font.Font(None, 64)



    def draw_timer(self):
        self.surface_title = self.font_title.render(str(self.counter), True, (255, 255, 255))
        self.rect_title = self.surface_title.get_rect()
        self.rect_title.center = (self.width / 1.10, (self.height / 9) + 1)
        self.screen.blit(self.surface_title, self.rect_title)


