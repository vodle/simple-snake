import pygame
import random

RES = 800
SIZE = 50

x, y = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)

length = 1
snake = [(x, y)]
dx, dy = 0, 0
speed = 5
dirs = {'W' : True, 'S' : True, 'A' : True, 'D' : True}

pygame.init()
display = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

while True:
    display.fill(pygame.Color('black'))
    [(pygame.draw.rect(display, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(display, pygame.Color('red'), (*apple, SIZE, SIZE))
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]
    if snake[-1] == apple:
        apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
        length += 1
        speed += 1

    if x < 0:
        x = RES
    if x > RES:
        x = 0
    if y < 0:
        y = RES
    if y > RES:
        y = 0

    if len(snake) != len(set(snake)):
        break


    pygame.display.flip()
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
