import pygame, random
from pygame.locals import *
import time

def on_grid_random():
    x = random.randint(0,390)
    y = random.randint(0,390)
    return (x//10 * 10, y//10 * 10)

def on_grid_random1():
    x = random.randint(0,390)
    y = random.randint(0,390)
    return (x//10 * 10, y//10 * 10)


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

X = on_grid_random1()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

bonus_pos = (500,500)
bonus = pygame.Surface((10,10))
bonus.fill((0,0,255))


my_direction = LEFT

clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
score = 0
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN  and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 5


    
    if score % 10 == 0 and score != 0:
    	bonus_pos = X 

    if collision(snake[0], bonus_pos):
        score += 21
        bonus_pos = (500,500)
        X = on_grid_random1()
        snake.append((0,0))        
        snake.append((0,0))
        snake.append((0,0))
        snake.append((0,0))
        snake.append((0,0))



    if snake[0][0] == 400 or snake[0][1] == 400 or snake[0][0] < 0 or snake[0][1] < 0:
    	pygame.quit()
    	exit()    

    for i in range(1, len(snake) -1):
    	if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
    		pygame.quit()
    		exit()

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    screen.blit(bonus, bonus_pos)


    for pos in snake:
        screen.blit(snake_skin,pos)


    for x in range(0, 400, 10):
    	pygame.draw.line(screen, (40,40,40), (x,0), (x,400))
    for y in range(0,400,10):
    	pygame.draw.line(screen,(40,40,40), (0,y), (400, y))


    	score_font = font.render('Score: %s' %(score), True, (255,255,255))
    	score_rect = score_font.get_rect()
    	screen.blit(score_font, score_rect)

    pygame.display.update()
