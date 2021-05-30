import pygame
from pygame.locals import *

import sys
import os

pygame.init()

screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

snake_logo = pygame.image.load(os.path.join("assets", "Start.png"))
message = pygame.image.load(os.path.join("assets", "start_screen_message.png"))

message_frames = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            pass

    screen.fill((0, 0, 0))
    screen.blit(snake_logo, (0, 0))

    message_frames += 1
    if message_frames > 30:
        screen.blit(message, (180, 562))

    if message_frames > 60:
        message_frames = 0

    pygame.display.flip()
    clock.tick(60)
