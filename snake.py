import pygame
import time
import random

# Initialize pygame
pygame.init()

# Game window dimensions
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game by ChatGPT")

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake parameters
snake_block = 10
snake_speed = 15

# Fonts and clock
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    win.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(win, green, [block[0], block[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])


def game_loop():
    game_over = False
    game_close = False

    # Initial snake position
    x, y = width / 2, height / 2
    x_change, y_change = 0, 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food coordinates
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            win.fill(blue)
            message("You Lost! Press Q-Quit or R-Play Again", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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

        # Boundary check: Game over if snake hits the walls
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        win.fill(black)

        pygame.draw.rect(win, blue, [food_x, food_y, snake_block, snake_block])
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Game over if snake collides with its own body
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        pygame.display.update()

        # Snake eats food, grows in length
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Start the game
game_loop()
