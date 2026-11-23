import pygame



class Options():
    def __init__(self, screen, settings):
        #self.pygame.mixer.music.load('music_and_sound/epic_action_music.mp3')
        #self.pygame.mixer.music.play(-1, 0.0)

        self.settings = settings
        self.screen = screen

        self.mouse = pygame.mouse.get_pos()

        self.image_button_back = pygame.image.load('images/button_back.png')
        self.image_button_back = pygame.transform.scale(self.image_button_back, (100, 100))

        self.bg_image = pygame.image.load('images/menu_bg.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (800, 650))

        self.image_sound_on = pygame.image.load('images/sound_on.png')
        self.image_sound_on = pygame.transform.scale(self.image_sound_on, (100, 100))

        self.image_sound_initial = pygame.image.load('images/sound_on.png')
        self.image_sound_initial = pygame.transform.scale(self.image_sound_on, (100, 100))

        self.image_music_on = pygame.image.load('images/music_on.png')
        self.image_music_on = pygame.transform.scale(self.image_music_on, (100, 150))

        self.image_music_initial = pygame.image.load('images/music_on.png')
        self.image_music_initial = pygame.transform.scale(self.image_music_on, (100, 150))

        self.image_sound_off = pygame.image.load('images/sound_off.png')
        self.image_sound_off = pygame.transform.scale(self.image_sound_off, (100, 100))

        self.image_music_off = pygame.image.load('images/music_off.png')
        self.image_music_off = pygame.transform.scale(self.image_music_off, (100, 150))

        self.size = screen.get_size()
        self.width = self.size[0]
        self.height = self.size[1]

        self.title = pygame.Rect(
            ((self.width / 16) + 1, (self.height / 8) + 1, 7 * self.width / 8, self.height / 4))

        self.font_title = pygame.font.Font(None, 64)


        # Creates and draws the text.
        self.surface_title = self.font_title.render('Game Option', True, (200, 0, 0))
        self.rect_title = self.surface_title.get_rect()  # get_rect() transfer to rectangle
        self.rect_title.center = (self.width / 2, (self.height / 4) + 1)

        self.sound_option = pygame.Rect(
            (self.width / 2.85, self.height / 2.32, self.width / 7, self.height / 7))
        self.music_option = pygame.Rect(
            (self.width / 1.632, self.height / 2.6, self.width / 8, self.height / 4))
        self.button_back_option = pygame.Rect((0, 0, self.width / 8, self.height / 6.5))

        self.rect_sound_on = self.image_sound_on.get_rect()
        self.rect_sound_on.center = (self.width / 2.5, (self.height / 2))
        self.rect_sound_off = self.image_sound_off.get_rect()
        self.rect_sound_off.center = (self.width / 6, (self.height / 2))
        self.rect_music_on = self.image_music_off.get_rect()
        self.rect_music_on.center = (self.width / 1.5, (self.height / 2))
        self.rect_music_off = self.image_music_off.get_rect()
        self.rect_music_off.center = (self.width / 1.2, (self.height / 2))
        self.rect_button_back = self.image_button_back.get_rect()
        self.rect_button_back.center = (0, 0)

    def draw_menu(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.image_button_back, (0, 0))
        self.screen.blit(self.surface_title, self.rect_title)
        self.screen.blit(self.image_sound_on, self.rect_sound_on)
        #print(self.rect_sound_on, self.rect_music_on)
        #print(self.sound_option, self.music_option)
        #print(self.rect_button_back)
        self.screen.blit(self.image_music_on, self.rect_music_on)
        #print(self.mouse)

