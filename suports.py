import pygame
import sys
import json


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


def load_high_score():
    try:
        open("save.json", "x")
    except IOError:
        pass
    score_file = open("save.json", "r")
    score = score_file.readline()
    if score:
        score = json.loads(score)["high_score"]
    else:
        score_file.close()
        score_file = open("save.json", "w")
        score = 0
        score_file.write(json.dumps({"high_score": 0}))
        score_file.close()

    return score


def save_high_score(score):
    score_file = open("save.json", "w")
    score_file.write(json.dumps({"high_score": score}))
    score_file.close()
