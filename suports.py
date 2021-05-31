import pygame
import sys


# text function
def draw_text(text_value, x, y, font_size, color, screen):
    font = pygame.font.Font('assets/VT323-Regular.ttf', font_size)
    text = font.render(text_value, False, color)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)


# rgb function
def color_variation(color):
    if color.hsla[0] < 359:
        color.hsla = color.hsla[0] + 1, color.hsla[1], color.hsla[2], color.hsla[3]
    else:
        color.hsla = 0, color.hsla[1], color.hsla[2], color.hsla[3]
    return color

def option_choice(current_text, current_option, screen, options_color):
    # looping for current option
    for index, option in enumerate(current_text):
        if index == current_option:
            draw_text(option[0], option[1], option[2], option[3], color_variation(options_color), screen)
        else:
            draw_text(option[0], option[1], option[2], option[3], option[4], screen)



def quit_game():
    pygame.quit()
    sys.exit()
