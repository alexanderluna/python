# Snake Game
import pygame
import sys
import random
import time

check_errors = pygame.init()
if check_errors[1] > 0:
    print("Had {0} errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("Pygame started successfully")

# set display size
playSurface = pygame.display.set_mode((720, 480))
# set display title
pygame.display.set_caption("Snake Game")

# set colors
red = pygame.Color(255, 0, 0) # game over
green = pygame.Color(0, 255, 0) # snake
black = pygame.Color(0, 0, 0) #screen
white = pygame.Color(255, 255, 255) #score
brown = pygame.Color(165, 42, 42) #food

# FPS controller
fpsController = pygame.time.Clock()

# Import variables
snakePos = [100,50]
snakeBody = [[100, 50],[90, 50],[80,50]]

# Food position
foodPos = [random.randrange(1, 72)*10, random.randrange(1, 48)*10]
foodRendered = True
