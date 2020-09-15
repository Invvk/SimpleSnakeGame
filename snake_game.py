import random

import pygame

pygame.init()

# colors
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
black = (0, 0, 0)

# font
font = pygame.font.SysFont("bellmt", 25)

# screen size 600x400
dis_width = 600
dis_height = 400

# Screen info
display = pygame.display.set_mode((dis_width, dis_height))

# Setting an application title
pygame.display.set_caption('Simple Snake Game')

# time
clock = pygame.time.Clock()

# snake info
snake_block = 20
snake_speed = 20

win = False

def current_score(score):
    value = font.render("Your Score: " + str(score), True, red)
    display.blit(value, (0, 0))

def message(msg, height, width, color):
    value = font.render(msg, True, color)
    display.blit(value, (dis_height / height, dis_width / width))

def draw_snake(snake_blocks, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_blocks, snake_blocks])

def return_range(value, expected):
    if value >= expected:
        return expected - 20
    else:
        return value

def game():
    global win
    ended = False
    game_close = False

    x = dis_width / 2
    y = dis_height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_size = 1

    food_x = return_range(20 * round(random.randrange(0, dis_height) / 20), 600)
    food_y = return_range(20 * round(random.randrange(0, dis_height) / 20), 400)

    while not ended:

        while win:
            display.fill(black)
            score = snake_size - 1
            # highet , width
            message("You Won! Score: " + str(score), 2, 7, white)
            message("Press Q to quit, Press R to retry", 3, 6, white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ended = True
                    game_close = False
                    win = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        ended = True
                        game_close = False
                        win = False
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_r:
                        win = False
                        game()
        while game_close:
            display.fill(black)
            score = snake_size - 1
            # highet , width
            message("You Lost! Score: " + str(score), 2, 7, white)
            message("Press Q to quit, Press R to retry", 3, 6, white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ended = True
                    game_close = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        ended = True
                        game_close = False
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_r:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ended = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            game_close = True

        x += x_change
        y += y_change

        display.fill(white)
        pygame.draw.rect(display, green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_size:
            del snake_list[0]

        for x1 in snake_list[:-1]:
            if x1 == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        current_score(snake_size - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = return_range(20 * round(random.randrange(0, dis_height) / 20), 600)
            food_y = return_range(20 * round(random.randrange(0, dis_height) / 20), 400)
            snake_size += 450
            if snake_size >= 450:
                win = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game()
