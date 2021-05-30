import pygame

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
