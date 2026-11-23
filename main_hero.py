import pygame
from pygame.sprite import Sprite


class Main_hero(Sprite):

    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/mainHeroSkins/rightSide/right_moving1.png')
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()


        self.rect.centery = self.screen_rect.centery + 236
        self.rect.centerx = self.screen_rect.centerx + 5

        self.reload = False
        self.fast_run_reload = True
        self.wait_for_reload = False
        self.custom_timer = 0
        self.fast_run_custom_timer = 0


        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.last_position = 4

        self.back_images = ['images/mainHeroSkins/backSide/BackSide1.png', 'images/mainHeroSkins/backSide/BackSide2.png', 'images/mainHeroSkins/backSide/BackSide3.png',
                            'images/mainHeroSkins/backSide/BackSide4.png', 'images/mainHeroSkins/backSide/BackSide5.png', 'images/mainHeroSkins/backSide/BackSide6.png',
                            'images/mainHeroSkins/backSide/BackSide7.png', 'images/mainHeroSkins/backSide/BackSide8.png', 'images/mainHeroSkins/backSide/BackSide9.png',
                            'images/mainHeroSkins/backSide/BackSide10.png']

        self.front_images = ['images/mainHeroSkins/frontSide/FrontSide1.png', 'images/mainHeroSkins/frontSide/FrontSide2.png', 'images/mainHeroSkins/frontSide/FrontSide3.png',
                            'images/mainHeroSkins/frontSide/FrontSide4.png', 'images/mainHeroSkins/frontSide/FrontSide5.png', 'images/mainHeroSkins/frontSide/FrontSide6.png',
                            'images/mainHeroSkins/frontSide/FrontSide7.png', 'images/mainHeroSkins/frontSide/FrontSide8.png', 'images/mainHeroSkins/frontSide/FrontSide9.png',
                            'images/mainHeroSkins/frontSide/FrontSide10.png']

        self.left_images = ['images/mainHeroSkins/leftSide/left_moving1.png', 'images/mainHeroSkins/leftSide/left_moving2.png',
                            'images/mainHeroSkins/leftSide/left_moving1.png', 'images/mainHeroSkins/leftSide/left_moving2.png',
                            ]

        self.right_images = ['images/mainHeroSkins/rightSide/right_moving1.png', 'images/mainHeroSkins/rightSide/right_moving2.png',
                             'images/mainHeroSkins/rightSide/right_moving1.png', 'images/mainHeroSkins/rightSide/right_moving2.png',
                             'images/mainHeroSkins/rightSide/right_moving1.png', 'images/mainHeroSkins/rightSide/right_moving2.png',
                             'images/mainHeroSkins/rightSide/right_moving1.png', 'images/mainHeroSkins/rightSide/right_moving2.png',
                             'images/mainHeroSkins/rightSide/right_moving1.png', 'images/mainHeroSkins/rightSide/right_moving2.png']

        self.left_right_run = ['images/mainHeroSkins/leftRightRun/leftRightRun1.png', 'images/mainHeroSkins/leftRightRun/leftRightRun2.png', 'images/mainHeroSkins/leftRightRun/leftRightRun3.png',
                            'images/mainHeroSkins/leftRightRun/leftRightRun4.png','images/mainHeroSkins/leftRightRun/leftRightRun5.png','images/mainHeroSkins/leftRightRun/leftRightRun6.png']

        self.back_run = ['images/mainHeroSkins/backRun/BackRun1.png','images/mainHeroSkins/backRun/BackRun2.png','images/mainHeroSkins/backRun/BackRun3.png','images/mainHeroSkins/backRun/BackRun4.png']

        self.front_run = ['images/mainHeroSkins/frontRun/FrontRun1.png','images/mainHeroSkins/frontRun/FrontRun2.png','images/mainHeroSkins/frontRun/FrontRun3.png','images/mainHeroSkins/frontRun/FrontRun4.png']

        self.anim_count = 0
        self.run_anim_count = 0
        self.fps = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        if self.moving_up or self.moving_down or self.moving_left or self.moving_right:
            pass
        else:
            if self.last_position == 2:
                if self.anim_count > len(self.back_images) - 1:
                    self.anim_count = 0
                self.image = pygame.image.load(self.back_images[self.anim_count])
                self.image = pygame.transform.scale(self.image, (40, 42))
                self.rect.width = self.image.get_rect().width
                self.rect.height = self.image.get_rect().height

                self.fps += 1

            elif self.last_position == 4:
                if self.anim_count > len(self.front_images) - 1:
                    self.anim_count = 0
                self.image = pygame.image.load(self.front_images[self.anim_count])
                self.image = pygame.transform.scale(self.image, (40, 42))
                self.rect.width = self.image.get_rect().width
                self.rect.height = self.image.get_rect().height
                self.fps += 1

            elif self.last_position == 3:
                if self.anim_count > len(self.right_images) - 1:
                    self.anim_count = 0
                self.image = pygame.image.load(self.right_images[self.anim_count])
                self.image = pygame.transform.scale(self.image, (40, 40))
                self.rect.width = self.image.get_rect().width
                self.rect.height = self.image.get_rect().height
                self.fps += 1

            elif self.last_position == 1:
                if self.anim_count > len(self.left_images) - 1:
                    self.anim_count = 0
                self.image = pygame.image.load(self.left_images[self.anim_count])
                self.image = pygame.transform.scale(self.image, (40, 40))
                self.rect.width = self.image.get_rect().width
                self.rect.height = self.image.get_rect().height
                self.fps += 1

            if self.fps > 9:
                self.anim_count += 1
                self.fps = 0
                if self.anim_count > len(self.front_images) - 1:
                    self.anim_count = 0

    def update(self, collide, hero, blocks):
         self.portal()
         moving = self.moving_right or self.moving_left or self.moving_down or self.moving_up
         if moving:
             if collide and self.last_position == 1:
                 self.rect.x += 1
                 self.moving_left = False

             if collide and self.last_position == 2:
                 self.rect.y += 1
                 self.moving_up = False

             if collide and self.last_position == 3:
                 self.rect.x -= 1
                 self.moving_right = False

             if collide and self.last_position == 4:
                 self.rect.y -= 1
                 self.moving_down = False

             else:
                 if self.moving_left and self.rect.left > self.screen_rect.left:                # Number 1

                    self.last_position = 1
                    self.rect.centerx -= self.settings.main_hero_speed
                    if self.run_anim_count > len(self.left_right_run) - 1:
                        self.run_anim_count = 0
                    if pygame.sprite.spritecollide(hero, blocks, False
                                                ):
                        self.rect.centerx += self.settings.main_hero_speed
                    else:
                        self.image = pygame.image.load(self.left_right_run[self.run_anim_count])
                        self.image = pygame.transform.flip(self.image, 1, 0)
                        self.image = pygame.transform.scale(self.image, (40, 40))
                        self.rect.width = self.image.get_rect().width
                        self.rect.height = self.image.get_rect().height
                        self.fps += 1



                 if self.moving_up and self.rect.top > self.screen_rect.top:                     # Number 2
                    self.last_position = 2
                    self.rect.centery -= self.settings.main_hero_speed
                    if self.run_anim_count > len(self.back_run) - 1:
                        self.run_anim_count = 0
                    if pygame.sprite.spritecollide(hero, blocks, False
                                                ):
                        self.rect.centery += self.settings.main_hero_speed
                    else:
                        self.image = pygame.image.load(self.back_run[self.run_anim_count])
                        self.image = pygame.transform.scale(self.image, (40, 40))
                        self.rect.width = self.image.get_rect().width
                        self.rect.height = self.image.get_rect().height
                        self.fps += 1



                 if self.moving_right and self.rect.right < self.screen_rect.right:               # Number 3
                    self.last_position = 3
                    self.rect.centerx += self.settings.main_hero_speed
                    if self.run_anim_count > len(self.left_right_run) - 1:
                        self.run_anim_count = 0
                    if pygame.sprite.spritecollide(hero, blocks, False
                                                ):
                        self.rect.centerx -= self.settings.main_hero_speed
                    else:
                        self.image = pygame.image.load(self.left_right_run[self.run_anim_count])
                        self.image = pygame.transform.scale(self.image, (40, 40))
                        self.rect.width = self.image.get_rect().width
                        self.rect.height = self.image.get_rect().height
                        self.fps += 1

                 if self.moving_down and self.rect.bottom < self.screen_rect.height:               # Number 4
                    self.last_position = 4
                    self.rect.centery += self.settings.main_hero_speed

                    if self.run_anim_count > len(self.front_run) - 1:
                        self.run_anim_count = 0
                    if pygame.sprite.spritecollide(hero, blocks, False
                                                ):
                        self.rect.centery -= self.settings.main_hero_speed
                    else:
                        self.image = pygame.image.load(self.front_run[self.run_anim_count])
                        self.image = pygame.transform.scale(self.image, (40, 40)).convert_alpha()
                        self.fps += 1


                 if self.fps > 9:
                     self.run_anim_count += 1
                     self.fps = 0
                     if self.run_anim_count > len(self.left_right_run) - 1:
                         self.run_anim_count = 0


    def portal(self):
        '''Portal for transition in room'''
        if 70 <= self.rect.centerx <= 155 and 86 <= self.rect.centery <= 96 and self.settings.level == 1:
            self.settings.level = 2
            self.settings.key_plots = 1

            self.rect.centery = self.screen_rect.centery + 232
            self.rect.centerx = self.screen_rect.centerx + 5

        elif 268 <= self.rect.centerx <= 338 and 266 <= self.rect.centery <= 279 and self.settings.level == 2:
            self.settings.level = 3

            self.rect.centery = self.screen_rect.centery + 232
            self.rect.centerx = self.screen_rect.centerx + 5

        '''Portal for plot'''

        if 525 <= self.rect.centerx <= 530 and 525 <= self.rect.centery <= 605 and self.settings.level == 1 :    # First wizard plot
            self.settings.plot_photo = 1

        elif 257 <= self.rect.centerx <= 387 and 350 <= self.rect.centery <= 470 and self.settings.level == 2:  # Second wizard plot
            self.settings.plot_photo = 2

    def fast_run_need_reload(self):
        if self.fast_run_reload == False:
            self.fast_run_custom_timer += 1
            #print(self.fast_run_custom_timer)
            if self.fast_run_custom_timer > 500:
                self.fast_run_reload = True
                self.fast_run_custom_timer = 0


