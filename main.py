import pygame
import game_functions as g_f
from settings import Settings
from main_hero import Main_hero
from pygame.sprite import Group
from game_menu import Game_menu
from Options import Options
from pause_menu import Pause_menu
from collides_block_create import create_blocks_first_room
from collides_block_create import create_blocks_second_room
from collides_block_create import create_blocks_third_room
from collides_block_create import create_blocks_fourst_room
from custom_timer import Custom_timer
from npc_bot import Enemy
from wizard import Wizard
from secondWizard import MagicWizard
from Boss import BossEnemy


def run_game():
    pygame.init()
    pygame.mixer.init()
    game_settings = Settings()
    arrows = Group()
    blocks = Group()

    screen = pygame.display.set_mode(
        (
            game_settings.screen_width,
            game_settings.screen_height
        )
    )

    menu = Game_menu(screen, game_settings)
    options = Options(screen, game_settings)
    pause = Pause_menu(screen, game_settings)
    custom_timer = Custom_timer(screen, game_settings)

    secondWizard = MagicWizard(screen)
    wizard = Wizard(screen)
    main_hero = Main_hero(screen, game_settings)
    enemy = Enemy(screen, game_settings)
    boss = BossEnemy(screen)

    """Maps or backgrounds"""

    background_image1 = pygame.image.load('images/backgroundMapsAndItems/mapBackGround/map_balcon.png')
    background_image2 = pygame.image.load('images/backgroundMapsAndItems/mapBackGround/map_hall.png')
    background_image3 = pygame.image.load('images/backgroundMapsAndItems/mapBackGround/map_boss.png')
    background_image4 = pygame.image.load('images/backgroundMapsAndItems/mapBackGround/game_over.png')

    """Details (colons, zabors.)"""

    colona = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/colona.png').convert_alpha()
    colona2 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/colona.png').convert_alpha()
    colona3 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/half_colona.png').convert_alpha()
    colona4 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/half_colona.png').convert_alpha()

    zabor_1 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/zabor.png').convert_alpha()
    zabor_2 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/zabor_2.png').convert_alpha()
    zabor_3 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/zabor_3.png').convert_alpha()
    zabor_4 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/zabor_4.png').convert_alpha()
    zabor_5 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/zabor_5.png').convert_alpha()
    zabor_6 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/zabor_6.png').convert_alpha()
    zabor_7 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/zabor_7.png').convert_alpha()
    zabor_8 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/zabor_8.png').convert_alpha()
    zabor_9 = pygame.image.load('images/backgroundMapsAndItems/backGroundItems/zabor_9.png').convert_alpha()

    firstPlot = pygame.image.load('images/plots/firstPlotPhoto.png').convert_alpha()
    secondPlot = pygame.image.load('images/plots/secondPlotPhoto.png').convert_alpha()

    iconWithFireBall = pygame.image.load('images/fireballs/amount/iconWithFireball.png').convert_alpha()
    iconWithoutFireBall = pygame.image.load('images/fireballs/amount/iconWithoutFireBall.png').convert_alpha()


    background_image1 = pygame.transform.scale(background_image1, (608, 736)).convert()
    background_image2 = pygame.transform.scale(background_image2, (608, 736)).convert()
    background_image3 = pygame.transform.scale(background_image3, (608, 736)).convert()
    background_image4 = pygame.transform.scale(background_image4, (608, 736)).convert()

    '''Music'''

    pygame.mixer.music.load("music_and_sound/epic_action_music.wav")
    pygame.mixer.music.play()

    '''Title'''

    pygame.display.set_caption("Легендарний Годвин")
    clock = pygame.time.Clock()

    while True:
            # Windows on menu (settings, menu)
        if game_settings.game_start == 0 and game_settings.game_options == 0:
            menu.draw_menu()
            pygame.display.flip()
            g_f.check_menu_events(game_settings, menu)

        elif game_settings.game_start == 0 and game_settings.game_options == 1:
            options.draw_menu()
            pygame.display.flip()
            g_f.check_menu_options_events(game_settings, options)

        elif game_settings.game_start == 1 and game_settings.game_resume == 1:

            pause.draw_menu()
            pygame.display.flip()
            g_f.check_menu_pause_events(game_settings, pause)

        elif game_settings.game_start == 1 and game_settings.game_resume == 0:
            g_f.check_events(main_hero, arrows, screen, game_settings, custom_timer)

            main_hero.update(pygame.sprite.spritecollide(main_hero, blocks, False), main_hero, blocks)

            arrows.update()
            clock.tick_busy_loop(60)






            if game_settings.level == 1:
                screen.blit(background_image1, (0, 0))
                create_blocks_first_room(blocks, screen)

            elif game_settings.level == 2:
                screen.blit(background_image2, (0, 0))
                blocks.empty()
                create_blocks_second_room(blocks, screen)

            elif game_settings.level == 3:
                blocks.empty()
                if custom_timer.counter > 60:
                    blocks.empty()
                    screen.blit(background_image4, (0, 0))
                    create_blocks_fourst_room(blocks, screen)
                else:
                    create_blocks_third_room(blocks, screen)
                    screen.blit(background_image3, (0, 0))
                    custom_timer.draw_timer()


          #  for block in blocks:
         #       block.draw_block()

            for arrow in arrows:
                if arrow.rect.bottom <= 0:
                    arrows.remove(arrow)
                elif arrow.rect.right <= 0:
                    arrows.remove(arrow)
                elif arrow.rect.left >= game_settings.screen_width:
                    arrows.remove(arrow)
                elif arrow.rect.top >= game_settings.screen_width:
                    arrows.remove(arrow)
            # print(main_hero.custom_timer)

            g_f.update_screen(screen, game_settings, main_hero, arrows, enemy, background_image1, background_image2, colona, colona2,
                              colona3,
                              colona4, zabor_1, zabor_2, zabor_3, zabor_4, zabor_5, zabor_6, zabor_7, zabor_8, zabor_9, wizard,
                              secondWizard, secondPlot, firstPlot, iconWithFireBall, iconWithoutFireBall, boss)


run_game()
