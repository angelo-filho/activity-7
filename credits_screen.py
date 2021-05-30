from pygame.locals import *

from suports import *

import os

credit = pygame.image.load(os.path.join("assets", "Credits.png"))
header_color = pygame.Color("#E16D2B")


def credits_screen(screen):
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            elif event.type == KEYDOWN:
                if event.key == K_c:
                    running = False

        screen.fill((0, 0, 0))
        screen.blit(credit, (0, 0))
        draw_text("DEVS", 300, 127, 62, color_variation(header_color), screen)
        pygame.display.flip()
        clock.tick(60)
