import pygame


class Pause_menu():
    def __init__(self, screen, settings):

        self.settings = settings
        self.screen = screen

        self.bg_image = pygame.image.load('images/menu_bg.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (800, 650))

        self.bg_button = pygame.image.load('images/button_bg.png')
        self.bg_button_rect = self.bg_button.get_rect()
        self.bg_button = pygame.transform.scale(self.bg_button, (385, 50))

        self.size = screen.get_size()
        self.width = self.size[0]
        self.height = self.size[1]

        self.title = pygame.Rect(
            ((self.width / 16) + 1, (self.height / 8) + 1, 7 * self.width / 8, self.height / 4))
        self.pause_menu_but1 = pygame.Rect(
            ((self.width / 4) + 1, (self.height / 2) + 1, 2 * self.width / 4, self.height / 10))
        self.pause_menu_but2 = pygame.Rect(((self.width / 4) + 1, (self.height / 2) + 1 + (3 * self.height / 20),
                                       2 * self.width / 4, self.height / 10))
        self.pause_menu_but3 = pygame.Rect(((self.width / 4) + 1, (self.height / 2) + 1 + (6 * self.height / 20),
                                            2 * self.width / 4, self.height / 10))

        self.font_resume_game = pygame.font.Font(None, 64)
        self.font_menu = pygame.font.Font(None, 32)

        self.surface_title = self.font_resume_game.render('Pause Menu', True, (139, 69, 19))
        self.rect_title = self.surface_title.get_rect()  # get_rect() transfer to rectangle
        self.rect_title.center = (self.width / 2, (self.height / 4) + 1)

        self.surface_resume_game = self.font_menu.render('RESUME GAME', True, (0, 0, 0))
        self.rect_resume_game = self.surface_resume_game.get_rect()
        self.rect_resume_game.center = (self.width / 2.05, (self.height / 2.05) + (self.height / 20) + 3)

        self.surface_options_game = self.font_menu.render('OPTIONS', True, (0, 0, 0))
        self.rect_options_game = self.surface_options_game.get_rect()
        self.rect_options_game.center = (self.width / 2.05, (self.height / 2.05) + (4 * self.height / 20) + 3)

        self.surface_exit_game = self.font_menu.render('EXIT GAME', True, (0, 0, 0))
        self.rect_exit_game = self.surface_exit_game.get_rect()
        self.rect_exit_game.center = (self.width / 2.05, (self.height / 2.05) + (7 * self.height / 20) + 3)

    def draw_menu(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.surface_title, self.rect_title)
        self.screen.blit(self.bg_button, (self.width / 5.75, (self.height / 2) + 5))
        self.screen.blit(self.bg_button, (self.width / 5.75, (self.height / 1.55) + 10))
        self.screen.blit(self.bg_button, (self.width / 5.75, (self.height / 1.25) + 5))
        self.screen.blit(self.surface_resume_game, self.rect_resume_game)
        self.screen.blit(self.surface_options_game, self.rect_options_game)
        self.screen.blit(self.surface_exit_game, self.rect_exit_game)