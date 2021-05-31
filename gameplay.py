import os

from pygame.locals import *
from constants import *
from suports import *
from pygame.math import Vector2

from random import randint
from end_game_screen import end_game_screen


def load_2x_img(dir_name, file_name):
    img = pygame.image.load(os.path.join(dir_name, file_name))
    img = pygame.transform.scale2x(img)

    return img


def random_pos(snake):
    pos_x = (randint(132, WINDOW - 32) // 32) * 32
    pos_y = (randint(132, WINDOW - 32) // 32) * 32

    for piece in snake:
        if Vector2(pos_x, pos_y) == piece:
            pos_x, pos_y = random_pos(snake)
            break

    return pos_x, pos_y


def create_grid(surface):
    for y in range(35):
        for x in range(35):
            r = pygame.Rect(x * 20, y * 20, 20, 20)
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, "#75CFF6", r)
            else:
                pygame.draw.rect(surface, "#51A8E8", r)


def create_wall(surface):
    pygame.draw.line(surface, "#3B7AD8", (16, 0), (16, 700), 32)
    pygame.draw.line(surface, "#3B7AD8", (0, 584), (700, 584), 32)
    pygame.draw.line(surface, "#3B7AD8", (0, 15), (700, 15), 32)
    pygame.draw.line(surface, "#3B7AD8", (690, 0), (690, 700), 32)


def head_movement(head, cur_dir):
    speed = 32
    if cur_dir == UP:
        head.update(head.x, head.y - speed)
    elif cur_dir == DOWN:
        head.update(head.x, head.y + speed)
    elif cur_dir == RIGHT:
        head.update(head.x + speed, head.y)
    elif cur_dir == LEFT:
        head.update(head.x - speed, head.y)


def snake_movement(snake, head):
    new_snake = [head]
    for i in range(1, len(snake)):
        new_snake.append(Vector2(snake[i - 1]))

    return new_snake


def snake_collision_with_walls(head):
    if head.x >= 700 - 32 or head.x < 32 or head.y >= 700 - 32 or head.y < 100:
        return True

    return False


def snake_self_collision(snake, head):
    for i in range(1, len(snake)):
        if head == snake[i]:
            return True

    return False


def draw_snake(screen, snake):
    for index, piece in enumerate(snake):
        if index == 0:
            continue

        if index < len(snake) - 1:
            screen.blit(snake_body, piece)


def draw_snakes_head(win, head, cur_dir):
    if cur_dir == UP:
        win.blit(snake_head_hor, head)
    elif cur_dir == DOWN:
        win.blit(pygame.transform.rotate(snake_head_hor, 180), head)
    elif cur_dir == RIGHT:
        win.blit(pygame.transform.rotate(snake_head, 180), head)
    elif cur_dir == LEFT:
        win.blit(snake_head, head)


def draw_snakes_tail(win, snake):
    if snake[-2].y < snake[-1].y:
        win.blit(snake_tail_hor, snake[-1])
    elif snake[-2].y > snake[-1].y:
        win.blit(pygame.transform.rotate(snake_tail_hor, 180), snake[-1])
    else:
        if snake[-2].x > snake[-1].x:
            win.blit(pygame.transform.rotate(snake_tail, 180), snake[-1])
        elif snake[-2].x < snake[-1].x:
            win.blit(snake_tail, snake[-1])


LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

snake_head = load_2x_img("assets", "snake_head.png")
snake_head_hor = load_2x_img("assets", "snake_head_hor.png")
snake_body = load_2x_img("assets", "snake_body.png")
snake_tail = load_2x_img("assets", "snake_tail.png")
snake_tail_hor = load_2x_img("assets", "snake_tail_hor.png")
apple = load_2x_img("assets", "apple.png")

pygame.mixer.init()

# https://freesound.org/people/MEAXX/sounds/218062/
bite_sound = pygame.mixer.Sound("sounds/bite__apple.wav")
# https://freesound.org/people/harrietniamh/sounds/415079/
death_sound = pygame.mixer.Sound("sounds/death-sound-effect.wav")


def gameplay(screen):
    current_dir = 1

    clock = pygame.time.Clock()

    # Setup snake
    head_pos = Vector2(320, 384)
    snake_pieces = [head_pos, Vector2(head_pos.x - 32, head_pos.y), Vector2(head_pos.x - 64, head_pos.y)]

    last_pos_y = 0
    new_pos_y = head_pos.y

    last_pos_x = 0
    new_pos_x = head_pos.x

    # Setup apple
    apple_pos = Vector2(random_pos(snake_pieces))

    bg = pygame.Surface([WINDOW, 600])
    # create_grid(bg)
    create_wall(bg)
    score = 0
    high_score = load_high_score()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            elif event.type == KEYDOWN:
                if event.key == K_UP and not current_dir == DOWN and not last_pos_x == new_pos_x:
                    current_dir = UP
                elif event.key == K_DOWN and not current_dir == UP and not last_pos_x == new_pos_x:
                    current_dir = DOWN
                elif event.key == K_LEFT and not current_dir == RIGHT and not last_pos_y == new_pos_y:
                    current_dir = LEFT
                elif event.key == K_RIGHT and not current_dir == LEFT and not last_pos_y == new_pos_y:
                    current_dir = RIGHT

        snake_pieces = snake_movement(snake_pieces, head_pos)
        head_movement(head_pos, current_dir)
        snake_collision_with_walls(head_pos)

        if head_pos == apple_pos:
            apple_pos = Vector2(random_pos(snake_pieces))
            snake_pieces.append(Vector2(snake_pieces[-1].x, snake_pieces[-1].y))
            score += 1
            bite_sound.play()

        last_pos_y = new_pos_y
        new_pos_y = head_pos.y

        last_pos_x = new_pos_x
        new_pos_x = head_pos.x

        screen.fill("#203BC7")
        draw_text(f"Score: {score}", 40, 0, 60, WHITE, screen)
        draw_text(f"H.Score: {high_score}", 370, 0, 60, WHITE, screen)
        screen.blit(bg, (0, 100))
        draw_snakes_head(screen, head_pos, current_dir)
        draw_snake(screen, snake_pieces)
        draw_snakes_tail(screen, snake_pieces)
        screen.blit(apple, apple_pos)

        if snake_self_collision(snake_pieces, head_pos) or snake_collision_with_walls(head_pos):
            if score > high_score:
                save_high_score(score)
            death_sound.play()
            pygame.time.wait(2000)
            restart = end_game_screen(screen)
            if restart:
                gameplay(screen)
            running = False

        pygame.display.flip()
        clock.tick(10)
