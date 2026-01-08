import pygame
import random

pygame.init()

W,H= 700,500
screen = pygame.display.set_mode((W,H)) 
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 35)


clock = pygame.time.Clock() #.  we use clock for speed limit
snake_block = 20
snake_speed = 10

def draw_text(text,color,x,y):
    screen.blit(font.render(text,True,color),(x,y)) #blit means draw

def game_loop():
    game_over = False
    game_close = False

    x = W // 2
    y= H // 2
    dx =0
    dy =0

    snake = []
    length = 1

    food_x = round(random.randrange(0,W-snake_block)/20) * 20
    food_y = round(random.randrange(0,H-snake_block)/20) * 20

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            draw_text("Game Over! Press C to play again or Q to Quit", RED,50,180)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        if x >= W or x < 0 or y >= H or y < 0:
            game_close = True

        x += dx
        y += dy
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])
        snake.append([x, y])
        if len(snake) > length:
            del snake[0]

        for block in snake[:-1]:
            if block == [x, y]:
                game_close = True

        for block in snake:
            pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

        draw_text(f"Score: {length - 1}", WHITE, 10, 10)
        pygame.display.update()

        snake_rect = pygame.Rect(x, y, snake_block, snake_block)
        food_rect = pygame.Rect(food_x, food_y, snake_block, snake_block)

        if snake_rect.colliderect(food_rect):
            food_x = round(random.randrange(0, W - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, H - snake_block) / snake_block) * snake_block
            length += 1


        clock.tick(snake_speed)

game_loop()
pygame.quit()
quit()


