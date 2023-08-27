import random
import pygame

# Initializing Pygame
pygame.init()

# Game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# properties for building snake
snake_size = 14
snake_speed = 7

# properties for the food
food_size = 20
food_color = BLUE

# Initial position of the snake
x = width // 2
y = height // 2

# Starting velocity
dx = 0
dy = 0

# Food instance
normal_food = None
special_food = None

# Starting position of the food
food_x = random.randint(0, width - food_size)
food_y = random.randint(0, height - food_size)

snake_score = 0
font = pygame.font.Font(None, 24)

snake_segments = []

Time = pygame.time.Clock()
timer_font = pygame.font.Font(None, 16)


def add_segment():
    snake_segments.append((0, 0))


def check_collision():
    if x < 0 or x + snake_size > width or y < 0 or y + snake_size > height:
        return True
    return False


# Timer
start_time = pygame.time.get_ticks()
game_duration = 60  # in secs
food_eaten = 0
max_food_eaten = 10

# Game loop
running = True
Game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not Game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -snake_speed
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = snake_speed
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -snake_speed
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = snake_speed
    if not Game_over:
        current_timing = pygame.time.get_ticks()
        elapsed_timing = (current_timing - start_time) // 1000

        if elapsed_timing >= game_duration:
            Game_over = True

        x += dx
        y += dy

        if x < food_x + food_size and x + snake_size > food_x and y < food_y + food_size and y + snake_size > food_y:
            snake_score += 1
            food_x = random.randint(0, width - food_size)
            food_y = random.randint(0, height - food_size)
            add_segment()

        if len(snake_segments) > 0:
            for i in range(len(snake_segments) - 1, 0, -1):
                snake_segments[i] = snake_segments[i - 1]
            snake_segments[0] = (x, y)

        if check_collision():
            Game_over = True

        window.fill(BLACK)

        pygame.draw.rect(window, GREEN, (x, y, snake_size, snake_size))
        for segment in snake_segments:
            pygame.draw.rect(window, GREEN, (segment[0], segment[1], snake_size, snake_size))

        pygame.draw.rect(window, food_color, (food_x, food_y, food_size, food_size))

        snake_score_text = font.render("Score:" + str(snake_score), True, GREEN)
        window.blit(snake_score_text, (10, 10))

        timer_text = timer_font.render("Time:" + str(game_duration - elapsed_timing), True, GREEN)
        window.blit(timer_text, (10, 30))
        pygame.display.update()
        Time.tick(30)

    else:
        window.fill(BLACK)
        Game_over_text = font.render("Game over", True, GREEN)
        snake_score_text = font.render("Score:" + str(snake_score), True, GREEN)
        window.blit(Game_over_text, (width // 2 - 100, height // 2 - 50))
        window.blit(snake_score_text, (width // 2 - 70, height // 2))
        pygame.display.update()

pygame.quit()
