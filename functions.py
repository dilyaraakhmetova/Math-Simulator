import random
import sys
import sympy
import pygame
import math
from button import ImageButton
from main import width, height, screen, bg_map


good_job = pygame.image.load("images/gj.png")
wrong_answer = pygame.image.load("images/wa.png")
final = pygame.image.load("images/final.png")
final = pygame.transform.scale(final, (800, 800))
right = pygame.mixer.Sound("right.mp3")
right.set_volume(0.1)
wrong = pygame.mixer.Sound("wrong.mp3")
win = pygame.mixer.Sound("win.mp3")
count = 0
def display_message_with_image(image):
    if image == good_job:
        right.play()
    elif image == wrong_answer:
        wrong.play()
    elif image == final:
        win.play()

    image_rect = image.get_rect(center=(width / 2, height / 2))
    screen.blit(image, image_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
def btn1():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")

    restart_required = False
    input_blocked = False
    global count

    operator = random.choice(['+', '-'])
    if operator == '+':
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        correct_answer = num1 + num2
    elif operator == '-':
        num1 = random.randint(30, 50)
        num2 = random.randint(10, 20)
        correct_answer = num1 - num2

    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 1", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        problem_font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
        if operator == '+':
            problem_text = f" {num1} + {num2} = ?"
        else:
            problem_text = f" {num1} - {num2} = ?"
        problem_surface = problem_font.render(problem_text, True, (255, 255, 255))
        problem_rect = problem_surface.get_rect(midtop=(width // 2, input_rect.bottom - 150))
        screen.blit(problem_surface, problem_rect)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count +=1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode


            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    operator = random.choice(['+', '-'])
                    if operator == '+':
                        num1 = random.randint(1, 20)
                        num2 = random.randint(1, 20)
                        correct_answer = num1 + num2
                    elif operator == '-':
                        num1 = random.randint(30, 50)
                        num2 = random.randint(10, 20)
                        correct_answer = num1 - num2
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            for btn in [back_button]:
                btn.handle_event(event)

        for btn in [back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn2():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")

    restart_required = False
    input_blocked = False
    global count

    operator = random.choice(['*', '/'])
    if operator == '/':
        while True:
            num1 = random.randint(50, 100)
            if sympy.isprime(num1):
                num1 = random.randint(30, 100)
            else:
                break
        numbers = sympy.divisors(num1)
        numbers.pop(numbers.index(1))
        numbers.pop(numbers.index(num1))
        num2 = random.choice(numbers)
        correct_answer = num1/num2
    else:
        num1 = random.randint(10, 19)
        num2 = random.randint(3, 9)
        while True:
            if num1 == num2:
                num2 = random.randint(5, 19)
            else:
                break
        correct_answer = num1*num2


    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 2", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        problem_font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
        if operator == '/':
            problem_text = f" {num1} / {num2} = ?"
        else:
            problem_text = f" {num1} * {num2} = ?"
        problem_surface = problem_font.render(problem_text, True, (255, 255, 255))
        problem_rect = problem_surface.get_rect(midtop=(width // 2, input_rect.bottom - 150))
        screen.blit(problem_surface, problem_rect)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    operator = random.choice(['*', '/'])
                    if operator == '/':
                        while True:
                            num1 = random.randint(50, 100)
                            if sympy.isprime(num1):
                                num1 = random.randint(30, 100)
                            else:
                                break
                        numbers = sympy.divisors(num1)
                        numbers.pop(numbers.index(1))
                        numbers.pop(numbers.index(num1))
                        num2 = random.choice(numbers)
                        correct_answer = num1 / num2
                    else:
                        num1 = random.randint(10, 19)
                        num2 = random.randint(3, 9)
                        while True:
                            if num1 == num2:
                                num2 = random.randint(5, 19)
                            else:
                                break
                        correct_answer = num1 * num2
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            for btn in [back_button]:
                btn.handle_event(event)

        for btn in [back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn3():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 600, 100)
    hint_rect.center = (width, 150)
    global count

    numbers = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    correct_answer = numbers[-1]
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 3", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface = font.render("Find next element of sequence", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 250))
        screen.blit(text_surface, text_rect)

        problem_font = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        problem_text = f"1, 3, 6, 10, 15, 21, 28, 36, 45, ..."
        problem_surface = problem_font.render(problem_text, True, (255, 255, 255))
        problem_rect = problem_surface.get_rect(midtop=(width // 2, input_rect.bottom - 150))
        screen.blit(problem_surface, problem_rect)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 30)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width-210, top=120)
            text_surface2 = font.render("3-1=2, 6-3=3, 10-6=4 ...", True, (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    numbers = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
                    correct_answer = numbers[-1]
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible


            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn4():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    global count
    hint_rect = pygame.Rect(0, 0, 1050, 100)
    hint_rect.center = (width, 150)

    correct_answer = 45 * 7
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 4", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface = font.render("Mark stays at a hostel in Paris for 7 nights,", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, input_rect.bottom - 175))
        screen.blit(text_surface, text_rect)

        problem_font = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        problem_text = ("and it costs $45 per night. How much does he spend in total?")
        problem_surface = problem_font.render(problem_text, True, (255, 255, 255))
        problem_rect = problem_surface.get_rect(midtop=(width // 2, input_rect.bottom - 150))
        screen.blit(problem_surface, problem_rect)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width - 250, top=130)
            text_surface2 = font.render("You should multiply the cost and amount of days", True, (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 45*7
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn5():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 300, 90)
    hint_rect.center = (width, 160)
    global count

    task5 = pygame.image.load("images/5.png")
    task5 = pygame.transform.scale(task5, (300, 150))
    correct_answer = 16
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 5", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface = font.render("Find the perimeter of this rectangle", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 200))
        screen.blit(text_surface, text_rect)

        task5_rect = task5.get_rect(center=(width / 2, 300))
        screen.blit(task5, task5_rect)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 30)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width - 90, top=130)
            text_surface2 = font.render("P = (a+b)*2", True, (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 16
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn6():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")


    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 1300, 100)
    hint_rect.center = (width, 150)
    global count

    correct_answer = 200*55-200*40
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 6", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 35)
        text_surface = font.render("John invested some money in stocks. He bought shares at $40 each and sold them at $55 each.", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, input_rect.bottom - 175))
        screen.blit(text_surface, text_rect)

        problem_font = pygame.font.Font("EdgeDisplay-Regular.otf", 35)
        problem_text = ("He purchased 200 shares and sold all of them. Calculate his profit.")
        problem_surface = problem_font.render(problem_text, True, (255, 255, 255))
        problem_rect = problem_surface.get_rect(midtop=(width // 2, input_rect.bottom - 150))
        screen.blit(problem_surface, problem_rect)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width - 300, top=130)
            text_surface2 = font.render("Subtract from the his earning from the sale how much he paid", True, (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 200*55-200*40
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn7():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 690, 100)
    hint_rect.center = (width, 150)
    global count

    task7 = pygame.image.load("images/7.png")
    task7 = pygame.transform.scale(task7, (200, 200))
    correct_answer = 60
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 7", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 40)
        text_surface = font.render("Find the area of this triangle", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 200))
        screen.blit(text_surface, text_rect)

        task7_rect = task7.get_rect(center=(width / 2, 280))
        screen.blit(task7, task7_rect)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width-130, top=130)
            text_surface2 = font.render("Use the formula Heron's formula", True,
                                        (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 60
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn8():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 1760, 120)
    hint_rect.center = (width, 170)
    global count

    correct_answer = 162/1.08
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 8", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 30)
        text_surface1 = font.render("The price of a product increased by 20%, then decreased by 10%. If after these changes", True, (255, 255, 255))
        text_rect1 = text_surface1.get_rect(center=(width/2, input_rect.bottom - 140))
        text_surface2 = font.render("the price of the product is $162, what was the original price of the product?", True,
                                    (255, 255, 255))
        text_rect2 = text_surface2.get_rect(center=(width/2, text_rect1.bottom + 25))
        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width-420, top=130)
            text_surface2 = font.render("Calculate the price after the 20% increase, then the final price after the 10% decrease,", True,
                                        (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            text_surface3 = font.render("and set up an equation using the given final price to find the original price.", True, (255, 255, 255))
            text_rect3 = text_surface3.get_rect(right=width, top=text_rect2.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)
            screen.blit(text_surface3, text_rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 150
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn9():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 1490, 120)
    hint_rect.center = (width, 170)
    global count

    correct_answer = 9
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 9", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 40)
        text_surface1 = font.render("In an arithmetic progression with the first term 7 and a common difference of 4,", True, (255, 255, 255))
        text_rect1 = text_surface1.get_rect(center=(width/2, input_rect.bottom - 165))
        text_surface2 = font.render("find the term number if its value is 39.", True,
                                    (255, 255, 255))
        text_rect2 = text_surface2.get_rect(center=(width/2, text_rect1.bottom + 25))
        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width-370, top=130)
            text_surface2 = font.render("Try to use the formula for the n-th term of an arithmetic progression and", True,
                                        (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            text_surface3 = font.render("set it equal to the given value of the term. Then solve the equation for n.", True, (255, 255, 255))
            text_rect3 = text_surface3.get_rect(right=width, top=text_rect2.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)
            screen.blit(text_surface3, text_rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 9
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn10():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 1400, 110)
    hint_rect.center = (width, 170)
    global count
    red_balls = 5
    blue_balls = 3
    green_balls = 2
    total_balls = red_balls + blue_balls + green_balls
    correct_answer = (red_balls + blue_balls) / total_balls * 100
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 10", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 40)
        text_surface1 = font.render("A bag contains 5 red balls, 3 blue balls, and 2 green balls. If a ball is randomly selected", True, (255, 255, 255))
        text_rect1 = text_surface1.get_rect(center=(width/2, input_rect.bottom - 140))
        text_surface2 = font.render("from the bag, what is the probability that it is either red or blue?(In '%')", True,
                                    (255, 255, 255))
        text_rect2 = text_surface2.get_rect(center=(width/2, text_rect1.bottom + 25))
        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width-350, top=130)
            text_surface2 = font.render("To find the probability of selecting a red or blue ball, divide the total", True,
                                        (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            text_surface3 = font.render("number of red and blue balls by the total number of balls in the bag.", True, (255, 255, 255))
            text_rect3 = text_surface3.get_rect(right=width, top=text_rect2.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)
            screen.blit(text_surface3, text_rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 80
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn11():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 1150, 120)
    hint_rect.center = (width, 170)
    global count

    correct_answer = 15
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 11", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 45)
        text_surface1 = font.render("Calculate the median of the set:", True, (255, 255, 255))
        text_rect1 = text_surface1.get_rect(center=(width/2, input_rect.bottom - 140))
        text_surface2 = font.render(" 4, 7, 7, 9, 12, 15, 15, 20, 20, 21", True,
                                    (255, 255, 255))
        text_rect2 = text_surface2.get_rect(center=(width/2, text_rect1.bottom + 25))
        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width-250, top=130)
            text_surface2 = font.render("Sort the numbers and select the middle one, or average", True,
                                        (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            text_surface3 = font.render("the two middle ones if there's an even count.", True, (255, 255, 255))
            text_rect3 = text_surface3.get_rect(right=width-60, top=text_rect2.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)
            screen.blit(text_surface3, text_rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 15
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn12():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 1120, 120)
    hint_rect.center = (width, 170)
    global count

    correct_answer = 21
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 12", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface1 = font.render("Find the GCD of 252 and 105.", True, (255, 255, 255))
        text_rect1 = text_surface1.get_rect(center=(width/2, input_rect.bottom - 140))
        screen.blit(text_surface1, text_rect1)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width-250, top=130)
            text_surface2 = font.render("Try applying the method of prime factorization to both", True, (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            text_surface3 = font.render("numbers to identify their common prime factors.", True, (255, 255, 255))
            text_rect3 = text_surface3.get_rect(right=width, top=text_rect2.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)
            screen.blit(text_surface3, text_rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 21
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn13():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 1200, 120)
    hint_rect.center = (width, 170)
    global count

    task13 = pygame.image.load("images/derivatives.png")
    task13 = pygame.transform.scale(task13, (400, 400))
    x = sympy.symbols('x')
    f = x ** 3 - 4 * x ** 2 + 2 * x - 7
    f_prime = sympy.diff(f, x)
    correct_answer = f_prime.subs(x, 3)
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 13", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 40)
        text_surface1 = font.render("Find the derivative and evaluate it at x = 3:", True, (255, 255, 255))
        text_rect1 = text_surface1.get_rect(center=(width/2, input_rect.bottom - 140))
        screen.blit(text_surface1, text_rect1)

        task13_rect = task13.get_rect(center=(width / 2, 330))
        screen.blit(task13, task13_rect)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width-300, top=130)
            text_surface2 = font.render("Differentiate each term of f(x) separately using the power ", True, (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            text_surface3 = font.render("rule, then evaluate the resulting expression at x = 3", True, (255, 255, 255))
            text_rect3 = text_surface3.get_rect(right=width-50, top=text_rect2.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)
            screen.blit(text_surface3, text_rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 5
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn14():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 900, 120)
    hint_rect.center = (width, 170)
    global count

    ways_case1 = sympy.binomial(8, 2) * sympy.binomial(10, 2)
    ways_case2 = sympy.binomial(8, 3) * sympy.binomial(10, 1)
    correct_answer = ways_case1 + ways_case2
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 14", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 30)
        text_surface1 = font.render("In a library, there are 10 mathematical books and 8 physics books on the shelf. How many ways can you select", True, (255, 255, 255))
        text_rect1 = text_surface1.get_rect(center=(width/2, input_rect.bottom - 140))
        text_surface2 = font.render("a set of 4 distinct books for reading, if there must be at least 2 physics books among them?", True,(255, 255, 255))
        text_rect2 = text_surface2.get_rect(center=(width / 2, text_rect1.bottom + 25))
        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width-200, top=130)
            text_surface2 = font.render("Choose 2 physics books from 8, then select", True, (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            text_surface3 = font.render("2 more books from the remaining collection.", True, (255, 255, 255))
            text_rect3 = text_surface3.get_rect(right=width, top=text_rect2.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)
            screen.blit(text_surface3, text_rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(good_job)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = 1820
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()
def btn15():
    back_button = ImageButton(0, 0, 100, 100, "", "images/back.png", "images/back1.png",
                              "click.wav")
    restart_button = ImageButton(0, 0, 100, 100, "", "images/restart.png", "images/restart.png", "click.wav")
    hint_button = ImageButton(1400, 0, 100, 100, "", "images/i.png", "images/i.1.png", "click.wav")

    restart_required = False
    input_blocked = False
    hint_text_visible = False
    hint_rect = pygame.Rect(0, 0, 1210, 120)
    hint_rect.center = (width, 170)
    global count

    task15 = pygame.image.load("images/integral.png")
    task15 = pygame.transform.scale(task15, (400, 400))
    x = sympy.symbols('x')
    integral_expr = 3 * x ** 2 + 2 * x - 5
    correct_answer = sympy.integrate(integral_expr, (x, 1, 4))
    user_input = ""

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_map, (0, 0))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 100)
        text_surface = font.render("Level 15", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 50))
        screen.blit(text_surface, text_rect)

        input_rect = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        font_input = pygame.font.Font("EdgeDisplay-Regular.otf", 50)
        text_surface_input = font_input.render(user_input, True, (255, 255, 255))
        screen.blit(text_surface_input, (input_rect.x + 5, input_rect.y + 5))

        font = pygame.font.Font("EdgeDisplay-Regular.otf", 45)
        text_surface1 = font.render("Calculate the definite integral from x = 1 to x = 4:", True, (255, 255, 255))
        text_rect1 = text_surface1.get_rect(center=(width/2, input_rect.bottom - 140))
        screen.blit(text_surface1, text_rect1)

        task15_rect = task15.get_rect(center=(width / 2, 330))
        screen.blit(task15, task15_rect)

        if restart_required:
            restart_button.rect.center = (width / 2, height - 100)
            restart_button.draw(screen)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 70)
            text_surface = font.render("Please, try again", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 600))
            screen.blit(text_surface, text_rect)

        if hint_text_visible:
            pygame.draw.rect(screen, (192, 139, 87), hint_rect)
            font = pygame.font.Font("EdgeDisplay-Regular.otf", 25)
            text_surface1 = font.render("Hint:", True, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(right=width-300, top=130)
            text_surface2 = font.render("Find the antiderivative of each term, then plug in the upper", True, (255, 255, 255))
            text_rect2 = text_surface2.get_rect(right=width, top=text_rect1.bottom + 10)
            text_surface3 = font.render("limit and subtract the result from plugging in the lower limit.", True, (255, 255, 255))
            text_rect3 = text_surface3.get_rect(right=width, top=text_rect2.bottom + 10)
            screen.blit(text_surface1, text_rect1)
            screen.blit(text_surface2, text_rect2)
            screen.blit(text_surface3, text_rect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if input_blocked:
                    continue
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(user_input)
                        if user_answer == correct_answer:
                            display_message_with_image(final)
                            input_blocked = True
                            count += 1
                        else:
                            display_message_with_image(wrong_answer)
                            restart_required = True
                            input_blocked = True
                    except ValueError:
                        pass
                    user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1):
                    user_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_required and restart_button.rect.collidepoint(event.pos):
                    correct_answer = sympy.integrate(integral_expr, (x, 1, 4))
                    restart_required = False
                    input_blocked = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                pass

            if event.type == pygame.USEREVENT and event.button == hint_button:
                hint_text_visible = not hint_text_visible

            for btn in [back_button, hint_button]:
                btn.handle_event(event)

        for btn in [back_button, hint_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()