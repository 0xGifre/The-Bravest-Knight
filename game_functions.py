import pygame
import sys
from pygame.locals import *
from arrow import Arrow
from game_menu import Game_menu
from settings import Settings
from Options import Options




def check_first_menuwww_events(settings, first_room, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if (first_room.pot.left < mouse[0] < first_room.pot.right) and (first_room.pot.top < mouse[1] < first_room.pot.bottom):
                settings.show_key = True
                if settings.show_key == True:
                    screen.blit(first_room.key_image, first_room.rect_key)
                else:
                    pass



def check_menu_pause_events(settings, pause):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            #print(mouse)
            if (pause.pause_menu_but1.left < mouse[0] < pause.pause_menu_but1.right) and (pause.pause_menu_but1.top < mouse[1] < pause.pause_menu_but1.bottom):
                settings.game_resume = 0
            elif (pause.pause_menu_but2.left < mouse[0] < pause.pause_menu_but2.right) and (pause.pause_menu_but2.top < mouse[1] < pause.pause_menu_but2.bottom):
                settings.game_options = 1
                settings.game_start = 0
            elif (pause.pause_menu_but3.left < mouse[0] < pause.pause_menu_but3.right) and (pause.pause_menu_but3.top < mouse[1] < pause.pause_menu_but3.bottom):
                sys.exit()



def check_menu_options_events(settings, options):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if (options.sound_option.left < mouse[0] < options.sound_option.right) and (options.sound_option.top < mouse[1] < options.sound_option.bottom):
                if options.image_sound_on == options.image_sound_off:
                    options.image_sound_on = options.image_sound_initial
                else:
                    options.image_sound_on = options.image_sound_off
            elif (options.music_option.left < mouse[0] < options.music_option.right) and (options.music_option.top < mouse[1] < options.music_option.bottom):
                if options.image_music_on == options.image_music_off:
                    options.image_music_on = options.image_music_initial
                    pygame.mixer.music.play()
                else:
                    options.image_music_on = options.image_music_off
                    pygame.mixer.music.stop()
            elif (options.button_back_option.left < mouse[0] < options.button_back_option.right) and (options.button_back_option.top < mouse[0] < options.button_back_option.bottom):
                settings.game_start = 0
                settings.game_options = 0



def check_menu_events(settings, menu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            #print(mouse)
            if (menu.start_menu_but1.left < mouse[0] < menu.start_menu_but1.right) and (menu.start_menu_but1.top < mouse[1] < menu.start_menu_but1.bottom):
                settings.game_start = 1
            elif (menu.start_menu_but2.left < mouse[0] < menu.start_menu_but2.right) and (menu.start_menu_but2.top < mouse[1] < menu.start_menu_but2.bottom):
                settings.game_options = 1  # Placeholder
            elif (menu.start_menu_but3.left < mouse[0] < menu.start_menu_but3.right) and (menu.start_menu_but3.top < mouse[1] < menu.start_menu_but3.bottom):
                sys.exit()  # Exits the game




def check_events(main_hero, arrows, screen, settings, timer,):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if settings.level == 3:
                timer.counter += 1
        elif event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(mouse)
            if settings.level == 1:
                if (413 < mouse[0] < 569 and 675 < mouse[1] < 715):
                    #print("WellCum")
                    settings.key_plots = 0
                    settings.plot_photo = 10
            elif settings.level == 2:
                if (413 < mouse[0] < 569 and 675 < mouse[1] < 715):
                    settings.key_plots = 0
                    settings.plot_photo = 20
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, main_hero, arrows, screen, settings)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, main_hero)





def update_screen(screen, settings, main_hero, arrows, enemy, background_image1, background_image2, colona, colona2, colona3, colona4, zabor_1,
                  zabor_2, zabor_3, zabor_4, zabor_5, zabor_6, zabor_7, zabor_8, zabor_9, wizard, secondWizard, secondPlot, firstPlot, iconWithFireBall, iconWithoutFireBall, boss):
    main_hero.blitme()
    if len(arrows) == 0:
        screen.blit(iconWithFireBall, (535, 700))
        screen.blit(iconWithFireBall, (560, 700))
        screen.blit(iconWithFireBall, (585, 700))
    elif len(arrows) == 1:
        screen.blit(iconWithFireBall, (535, 700))
        screen.blit(iconWithFireBall, (560, 700))
        screen.blit(iconWithoutFireBall, (585, 700))
    elif len(arrows) == 2:
        screen.blit(iconWithFireBall, (535, 700))
        screen.blit(iconWithoutFireBall, (560, 700))
        screen.blit(iconWithoutFireBall, (585, 700))
    elif len(arrows) == 3 :
        screen.blit(iconWithoutFireBall, (535, 700))
        screen.blit(iconWithoutFireBall, (560, 700))
        screen.blit(iconWithoutFireBall, (585, 700))

    if settings.level == 1:
        wizard.blitme()
        enemy.blitme()

        screen.blit(colona, (359, 361))
        screen.blit(colona2, (232, 361))
        screen.blit(colona3, (232, 535))
        screen.blit(colona4, (359, 535))
        screen.blit(zabor_6, (89, 163))
        screen.blit(zabor_7, (358, 163))
        screen.blit(zabor_8, (0, 345))
        screen.blit(zabor_9, (510, 345))

        if settings.plot_photo == 1 and settings.key_plots == 1:
            screen.blit(firstPlot, (0, 366))
            if settings.plot_photo == 10:
                screen.blit(background_image1, (0, 0))
                wizard.blitme()
                main_hero.blitme()

                screen.blit(colona, (359, 361))
                screen.blit(colona2, (232, 361))
                screen.blit(colona3, (232, 535))
                screen.blit(colona4, (359, 535))
                screen.blit(zabor_6, (89, 163))
                screen.blit(zabor_7, (358, 163))
                screen.blit(zabor_8, (0, 345))
                screen.blit(zabor_9, (510, 345))

    elif settings.level == 2:
        secondWizard.blitme()

        screen.blit(zabor_4, (126, 167))
        screen.blit(zabor_5, (475, 167))
        screen.blit(zabor_1, (186, 169))
        screen.blit(zabor_2, (475, 468))
        screen.blit(zabor_3, (33, 468))

        if settings.plot_photo == 2 and settings.key_plots == 1:
            screen.blit(secondPlot, (0, 366))
            if settings.plot_photo == 20:
                screen.blit(background_image2, (0, 0))
                secondWizard.blitme()
                main_hero.blitme()
                main_hero.fast_run()
                print(main_hero.custom_timer)

                screen.blit(zabor_4, (126, 167))
                screen.blit(zabor_5, (475, 167))
                screen.blit(zabor_1, (186, 169))
                screen.blit(zabor_2, (475, 468))
                screen.blit(zabor_3, (33, 468))
    elif settings.level == 3:
        boss.blitme()


    elif settings.plot_photo == 3:
        pass

    for arrow in arrows:
        arrow.draw_arrow()
    pygame.display.flip()


def check_keydown_events(event, main_hero, arrows, screen, settings):    # key which controlling hero

    if event.key == pygame.K_RIGHT or event.key == ord('d'):   # right
        main_hero.moving_right = True

    elif event.key == pygame.K_LEFT or event.key == ord('a'):  # left
        main_hero.moving_left = True

    elif event.key == pygame.K_UP or event.key == ord('w'):    # up
        main_hero.moving_up = True

    elif event.key == pygame.K_DOWN or event.key == ord('s'):  # down
        main_hero.moving_down = True



    elif event.key == pygame.K_SPACE and not main_hero.reload: # reload

        if len(arrows) < settings.arrow_allowed:
            new_arrow = Arrow(screen, settings, main_hero)
            arrows.add(new_arrow)
            sound = pygame.mixer.Sound("music_and_sound/arrow_sound.wav")    # arrow_sound
            sound.play()

    elif event.key == pygame.K_ESCAPE:       # menu_pause !
        settings.game_resume = 1

    elif event.key == pygame.K_q and main_hero.fast_run_reload == True:
        settings.main_hero_speed = 4
        main_hero.fast_run_reload = False


def check_keyup_events(event, main_hero):
    if event.key == pygame.K_RIGHT or event.key == ord('d'):  # right
        main_hero.moving_right = False

    elif event.key == pygame.K_LEFT or event.key == ord('a'): # left
        main_hero.moving_left = False

    elif event.key == pygame.K_UP or event.key == ord('w'):   # up
        main_hero.moving_up = False

    elif event.key == pygame.K_DOWN or event.key == ord('s'): # down
        main_hero.moving_down = False



