import pygame
import sys
from button import ImageButton
import functions as f

pygame.init()

width, height = 1500, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Math Simulator")
main_background = pygame.image.load("images/background1 (2).jpg")
main_background = pygame.transform.scale(main_background, (1500, 800))
bg_map = pygame.image.load("images/bg_main.jpg")
bg_map = pygame.transform.scale(bg_map, (1500, 800))
pygame.mixer.music.load("soundtrack.mp3")
pygame.mixer.music.play(-1)
global music_on
def main_menu():
    start_button = ImageButton(width / 2 - 427 / 2, 210, 427, 200, "Start", "images/button.png", "images/button1.png",
                               "click.wav")
    settings_button = ImageButton(width / 2 - 427 / 2, 330, 427, 200, "Settings", "images/button.png",
                                  "images/button1.png", "click.wav")
    exit_button = ImageButton(width / 2 - 427 / 2, 450, 427, 200, "Exit", "images/button.png", "images/button1.png",
                              "click.wav")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("MENU", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 150))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                new_game()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                setting_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for button in [start_button, settings_button, exit_button]:
                button.handle_event(event)

        for button in [start_button, settings_button, exit_button]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)

        pygame.display.flip()
def setting_menu():
    audio_button = ImageButton(width / 2 - 427 / 2, 210, 427, 200, "Audio", "images/button.png", "images/button1.png",
                               "click.wav")
    back_button = ImageButton(width / 2 - (252 / 2), 350, 252, 200, "Back", "images/button.png", "images/button1.png",
                              "click.wav")
    music_on = True
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 72)
        text_surface = font.render("SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 150))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.USEREVENT and event.button == audio_button:
                if music_on:
                    pygame.mixer.music.stop()
                    music_on = False
                else:
                    pygame.mixer.music.play(-1)
                    music_on = True

            for btn in [audio_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def new_game():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    button1 = ImageButton(50, 350, 80, 80, "1", "images/btn_lvl.png", "images/btn_lvl1.png", "click.wav")
    if f.count >= 1:
        button2 = ImageButton(149, 250, 80, 80, "2", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button2 = ImageButton(149, 250, 80, 80, "2", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 2:
        button3 = ImageButton(237, 150, 80, 80, "3", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button3 = ImageButton(237, 150, 80, 80, "3", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 3:
        button4 = ImageButton(325, 70, 80, 80, "4", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button4 = ImageButton(325, 70, 80, 80, "4", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 4:
        button5 = ImageButton(435, 70, 80, 80, "5", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button5 = ImageButton(435, 70, 80, 80, "5", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 5:
        button6 = ImageButton(523, 150, 80, 80, "6", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button6 = ImageButton(523, 150, 80, 80, "6", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 6:
        button7 = ImageButton(611, 250, 80, 80, "7", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button7 = ImageButton(611, 250, 80, 80, "7", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 7:
        button8 = ImageButton(700, 350, 80, 80, "8", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button8 = ImageButton(700, 350, 80, 80, "8", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 8:
        button9 = ImageButton(789, 450, 80, 80, "9", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button9 = ImageButton(789, 450, 80, 80, "9", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 9:
        button10 = ImageButton(877, 550, 80, 80, "10", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button10 = ImageButton(877, 550, 80, 80, "10", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 10:
        button11 = ImageButton(965, 630, 80, 80, "11", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button11 = ImageButton(965, 630, 80, 80, "11", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 11:
        button12 = ImageButton(1075, 630, 80, 80, "12", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button12 = ImageButton(1075, 630, 80, 80, "12", "images/btn_lvl_block.png", "images/btn_lvl_block1.png",
                           "click.wav")
    if f.count >= 12:
        button13 = ImageButton(1163, 530, 80, 80, "13", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button13 = ImageButton(1163, 530, 80, 80, "13", "images/btn_lvl_block.png", "images/btn_lvl_block1.png",
                           "click.wav")
    if f.count >= 13:
        button14 = ImageButton(1251, 430, 80, 80, "14", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button14 = ImageButton(1251, 430, 80, 80, "14", "images/btn_lvl_block.png", "images/btn_lvl_block1.png", "click.wav")
    if f.count >= 14:
        button15 = ImageButton(1340, 350, 80, 80, "15", "images/btn_lvl.png","images/btn_lvl1.png", "click.wav")
    else:
        button15 = ImageButton(1340, 350, 80, 80, "15", "images/btn_lvl_block.png", "images/btn_lvl_block1.png",
                           "click.wav")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("MAP", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                main_menu()

            if event.type == pygame.USEREVENT and event.button == button1:
                f.btn1()
                if f.count >= 1:
                    button2 = ImageButton(149, 250, 80, 80, "2", "images/btn_lvl.png", "images/btn_lvl1.png",
                                          "click.wav")

            if event.type == pygame.USEREVENT and event.button == button2:
                if f.count >= 1:
                    f.btn2()
                    if f.count >= 2:
                        button3 = ImageButton(237, 150, 80, 80, "3", "images/btn_lvl.png", "images/btn_lvl1.png",
                                              "click.wav")

            if event.type == pygame.USEREVENT and event.button == button3:
                if f.count >= 2:
                    f.btn3()
                    if f.count >= 3:
                        button4 = ImageButton(325, 70, 80, 80, "4", "images/btn_lvl.png", "images/btn_lvl1.png",
                                              "click.wav")

            if event.type == pygame.USEREVENT and event.button == button4:
                if f.count >=3:
                    f.btn4()
                    if f.count >= 4:
                        button5 = ImageButton(435, 70, 80, 80, "5", "images/btn_lvl.png", "images/btn_lvl1.png",
                                              "click.wav")

            if event.type == pygame.USEREVENT and event.button == button5:
                if f.count >=4:
                    f.btn5()
                    if f.count >= 5:
                        button6 = ImageButton(523, 150, 80, 80, "6", "images/btn_lvl.png", "images/btn_lvl1.png",
                                              "click.wav")

            if event.type == pygame.USEREVENT and event.button == button6:
                if f.count >= 5:
                    f.btn6()
                    if f.count >= 6:
                        button7 = ImageButton(611, 250, 80, 80, "7", "images/btn_lvl.png", "images/btn_lvl1.png",
                                              "click.wav")

            if event.type == pygame.USEREVENT and event.button == button7:
                if f.count >= 6:
                    f.btn7()
                    if f.count >= 7:
                        button8 = ImageButton(700, 350, 80, 80, "8", "images/btn_lvl.png", "images/btn_lvl1.png",
                                              "click.wav")

            if event.type == pygame.USEREVENT and event.button == button8:
                if f.count >= 7:
                    f.btn8()
                    if f.count >= 8:
                        button9 = ImageButton(789, 450, 80, 80, "9", "images/btn_lvl.png", "images/btn_lvl1.png",
                                              "click.wav")

            if event.type == pygame.USEREVENT and event.button == button9:
                if f.count >= 8:
                    f.btn9()
                    if f.count >= 9:
                        button10 = ImageButton(877, 550, 80, 80, "10", "images/btn_lvl.png", "images/btn_lvl1.png",
                                               "click.wav")

            if event.type == pygame.USEREVENT and event.button == button10:
                if f.count >= 9:
                    f.btn10()
                    if f.count >= 10:
                        button11 = ImageButton(965, 630, 80, 80, "11", "images/btn_lvl.png", "images/btn_lvl1.png",
                                               "click.wav")

            if event.type == pygame.USEREVENT and event.button == button11:
                if f.count >= 10:
                    f.btn11()
                    if f.count >= 11:
                        button12 = ImageButton(1075, 630, 80, 80, "12", "images/btn_lvl.png", "images/btn_lvl1.png",
                                               "click.wav")

            if event.type == pygame.USEREVENT and event.button == button12:
                if f.count >= 11:
                    f.btn12()
                    if f.count >= 12:
                        button13 = ImageButton(1163, 530, 80, 80, "13", "images/btn_lvl.png", "images/btn_lvl1.png",
                                               "click.wav")

            if event.type == pygame.USEREVENT and event.button == button13:
                if f.count >= 12:
                    f.btn13()
                    if f.count >= 13:
                        button14 = ImageButton(1251, 430, 80, 80, "14", "images/btn_lvl.png", "images/btn_lvl1.png",
                                               "click.wav")

            if event.type == pygame.USEREVENT and event.button == button14:
                if f.count >= 13:
                    f.btn14()
                    if f.count >= 14:
                        button15 = ImageButton(1340, 350, 80, 80, "15", "images/btn_lvl.png", "images/btn_lvl1.png",
                                               "click.wav")

            if event.type == pygame.USEREVENT and event.button == button15:
                if f.count >= 14:
                    f.btn15()

            for btn in [back_button, button1, button2, button3, button4, button5, button6, button7, button8, button9,
                        button10, button11, button12, button13, button14, button15]:
                btn.handle_event(event)

        for btn in [back_button, button1, button2, button3, button4, button5, button6, button7, button8, button9,
                    button10, button11, button12, button13, button14, button15]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
if __name__ == "__main__":
    main_menu()