# Import modules
import pygame
import sys
import random
import time

# check for errors when booting
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
black = pygame.Color(40, 40, 40) #screen
white = pygame.Color(255, 255, 255) #score
purple = pygame.Color(128,0,128) #food

# FPS controller
fpsController = pygame.time.Clock()

# Import variables
snakePos = [100,50]
snakeBody = [[100, 50],[90, 50],[80,50]]

# Food position
foodPos = [random.randrange(1, 72)*10, random.randrange(1, 48)*10]
foodRendered = True

# game score
score = 0
over = False

# direction
direction = 'RIGHT'
changeTo = direction

# define gameOver logic
def gameOver():
    showScore(True)
    myFont = pygame.font.SysFont('monaco', 72)
    gameOverColor = myFont.render("Game Over", True, red)
    gameOverRect = gameOverColor.get_rect()
    gameOverRect.midtop = (360, 15)
    playSurface.blit(gameOverColor, gameOverRect)

    pygame.display.flip()
    time.sleep(5)
    pygame.quit() #pygame exit
    sys.exit() #console exit

# render score
def showScore(over=False):
    myFont = pygame.font.SysFont('monaco', 28)
    scoreColor = myFont.render("Score: " + str(round(score, 2)), True, green)
    scoreRect = scoreColor.get_rect()
    if over:
        scoreRect.midtop = (360, 150)
    else:
        scoreRect.midtop = (80, 10)
    playSurface.blit(scoreColor, scoreRect)

# game loop
while True:
    # listen to events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # make sure snake can't go opposite direction
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # move the snake
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # grow Snake body after eating
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodRendered = False
        score += 10
    else:
        snakeBody.pop()
        score -= 0.01

    # update food position after eating
    if foodRendered == False:
        foodPos = [random.randrange(1, 72)*10, random.randrange(1, 48)*10]
    foodRendered = True

    playSurface.fill(black)

    # position the snake
    for pos in snakeBody:
        bodyObject = pygame.Rect(pos[0], pos[1], 10, 10)
        pygame.draw.rect(playSurface, green, bodyObject)

    # position the food
    foodObject = pygame.Rect(foodPos[0], foodPos[1], 10, 10)
    pygame.draw.rect(playSurface, purple, foodObject)

    # game over when hitting the wall
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 470 or snakePos[1] < 0:
        gameOver()

    # game over when hitting self
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    # game over when score is -5
    if score < -5:
        gameOver()

    showScore(over)
    pygame.display.flip()
    fpsController.tick(30)
