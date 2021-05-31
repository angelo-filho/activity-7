from suports import *
from pygame.locals import *
from constants import *


def end_game_screen(screen):
    is_running = True

    end_game_text = [("TRY AGAIN", 256, 451, 50, WHITE, screen), ("BACK TO MENU", 229, 516, 50, WHITE, screen)]
    current_option = 0
    options_color = pygame.Color(RED)

    while is_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            elif event.type == KEYDOWN:
                # getting action key
                if event.key == K_UP:
                    current_option -= 1
                    if current_option < 0:
                        current_option = 1
                elif event.key == K_DOWN:
                    current_option += 1
                    if current_option > 1:
                        current_option = 0
                elif event.key == K_SPACE:
                    if current_option == 0:
                        return True
                    elif current_option == 1:
                        is_running = False

        screen.fill(BLACK)

        draw_text("GAME", 114, 162, 122, YELLOW, screen)
        draw_text("OVER!!", 321, 164, 122, YELLOW, screen)

        option_choice(end_game_text, current_option, screen, options_color)

        pygame.display.flip()
