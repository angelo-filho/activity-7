from pygame.locals import *
from constants import *
from suports import *

from credits_screen import credits_screen
from gameplay import gameplay


def main_menu(screen):
    # setting basic stats for menu window
    fps = pygame.time.Clock()

    # setting texts for menu options
    menu_texts = [("PLAY", 307, 284, 48, WHITE, screen), ("CREDITS", 278, 347, 48, WHITE, screen),
                  ("EXIT", 306, 410, 48, WHITE, screen)]

    # value for text current orientation
    current_option = 0

    # verification for loop
    is_running = True

    # loading the instructions images
    instructions_left = pygame.image.load("assets/instructions_left.png")
    instructions_right = pygame.image.load("assets/instructions_right.png")

    # setting initial color for rgb
    menu_color = pygame.Color("#E16D2B")
    options_color = pygame.Color(RED)

    while is_running:

        # frames per second for window menu
        fps.tick(60)

        # getting the events in menu window
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            elif event.type == KEYDOWN:
                # getting action key
                if event.key == K_UP:
                    current_option -= 1
                    if current_option < 0:
                        current_option = 2
                elif event.key == K_DOWN:
                    current_option += 1
                    if current_option > 2:
                        current_option = 0
                # getting the select key
                elif event.key == K_SPACE:
                    if current_option == 0:
                        gameplay(screen)
                    elif current_option == 1:
                        credits_screen(screen)
                    elif current_option == 2:
                        quit_game()

        screen.fill(BLACK)

        # drawing the menu text
        draw_text("MENU", 276, 105, 92, menu_color, screen)
        # function for rgb text
        color_variation(menu_color)

        # calling the choice function
        option_choice(menu_texts, current_option, screen, options_color)

        # drawing the instructions
        screen.blit(instructions_left, (65, 630))
        screen.blit(instructions_right, (508, 630))

        pygame.display.flip()
