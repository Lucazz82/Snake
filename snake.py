import pygame
from sys import exit
from math import floor
from random import randrange
from tkinter import messagebox

# Functions ------------------------------------
def movement():
    for i, square in enumerate(game.snake):
        if len(game.directions) == (square.index):
            return

        if game.directions[i] == "up":
            square.rect.y -= speed
            square.row -= 1
        elif game.directions[i] == "down":
            square.rect.y += speed
            square.row += 1
        elif game.directions[i] == "left":
            square.rect.x -= speed
            square.column -= 1
        elif game.directions[i] == "right":
            square.rect.x += speed
            square.column += 1

def isValidDirection(direction):
    if game.directions[0] in ['up', 'down'] and direction in ['up', 'down']:
        return False

    if game.directions[0] in ['left', 'right'] and direction in ['left', 'right']:
        return False

    return True

def thereIsSnake(row, column):
    for body in game.snake:
        if row == body.row and column == body.column:
            return True
    
    return False
#-----------------------------------------------

# Pygame Setup
pygame.init()
clock = pygame.time.Clock()

# Display Setup
size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake By @Lucazz82")

# Grid Setup
menuHeight = 100
squareSize = 20
maxColumns = int(size[0] / squareSize)
maxRows = int((size[1] -menuHeight) / squareSize)

# Snake Setup
speed = squareSize

class Snake():
    def __init__(self, row, column, index):
        self.rect = pygame.Rect(column * squareSize, (row * squareSize) + menuHeight, squareSize, squareSize)
        self.row = row
        self.column = column
        self.direction = ''
        self.index = index

class Berry():
    def __init__(self):
        self.column = 0
        self.row = 0 
        self.rect = 0
        self.move()

    def move(self):
        while True:
            self.column = randrange(maxColumns)
            self.row = randrange(maxRows)

            if not thereIsSnake(self.row, self.column):
                break
        self.rect = pygame.Rect(self.column * squareSize, (self.row * squareSize) + menuHeight, squareSize, squareSize)

    def checkColision(self):
        if self.rect.colliderect(game.snake[0]):
            self.move()
            game.addBody()

class Game():
    def __init__(self):
        self.snake = []
        self.directions = []
        self.font = pygame.font.Font("freesansbold.ttf", 25)
        self.headDirection = ""
        self.snakeIcon = pygame.Rect(20, 20, 30, 30)
        self.initTime = pygame.time.get_ticks()

    def changeDirection(self):
        self.directions.insert(0, self.headDirection)
        if len(self.directions) > len(self.snake):
            self.directions.pop(-1)

    def addBody(self):
        pos = [self.snake[-1].row, self.snake[-1].column]
        self.snake.append(Snake(pos[0], pos[1], len(self.snake)))

    def checkColision(self):
        if self.snake[0].column < 0 or self.snake[0].column >= maxColumns:
            self.gameOver()
            return
        
        if self.snake[0].row < 0 or self.snake[0].row >= maxRows:
            self.gameOver()
            return

        # If the snake is less than 5 squares, cannot eat thenselve
        if len(self.snake) > 4:
            for body in self.snake[4:]:
                if self.snake[0].rect.colliderect(body.rect):
                    self.gameOver()
                    return

    def gameOver(self):
        print("Lose")
        self.directions.clear()
        messagebox.showinfo(title="Game Over", message="Your score is {} points.\nContratulations!".format(len(game.snake)))
        self.reset()

    def reset(self):
        self.__init__()
        self.snake.append(Snake(5,5, len(game.snake)))



# Game Setup
game = Game()
game.snake.append(Snake(5,5, len(game.snake)))
berry = Berry()

while True:
    # Handling Events
    for event in pygame.event.get():
        # Exit Game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if isValidDirection("up"):
                    game.headDirection = "up"
            if event.key == pygame.K_DOWN:
                if isValidDirection("down"):
                    game.headDirection = "down"
            if event.key == pygame.K_LEFT:
                if isValidDirection("left"):
                    game.headDirection = "left"
            if event.key == pygame.K_RIGHT:
                if isValidDirection("right"):
                    game.headDirection = "right"
            if event.key == pygame.K_SPACE:
                game.addBody()
                pass

    # Snake movement
    movement()
    game.changeDirection()

    # Colision -------------------------------------
    berry.checkColision()
    game.checkColision()
    # ----------------------------------------------
    
    # Visuals --------------------------------------
    # Background
    screen.fill((200,200,200))

    # Drawing The Grid
    for x in range(1, int(size[0] / squareSize)):
        pygame.draw.line(screen, (0,0,0), (squareSize * x, menuHeight), (squareSize * x, size[1]), 1)

    for y in range(int(size[1] / squareSize)):
        pygame.draw.line(screen, (0,0,0), (0, menuHeight + y * squareSize), (size[0], menuHeight + y * squareSize), 1)
    
    # Drawing Snake
    for square in game.snake:
        pygame.draw.rect(screen, (124,252,0), square.rect)

    # Drawing Snake Eyes
    pygame.draw.circle(screen, (0,0,0), (game.snake[0].column * squareSize + 5, game.snake[0].row * squareSize + menuHeight + 5), 2)
    pygame.draw.circle(screen, (0,0,0), (game.snake[0].column * squareSize + 15, game.snake[0].row * squareSize + menuHeight + 5), 2)
    
    # Drawing Berrys
    pygame.draw.rect(screen, (255,0,0), berry.rect)

    # Drawing Score
    length = game.font.render("x {}".format(len(game.snake)), True, (0,0,0))
    screen.blit(length, (60,25))
    pygame.draw.rect(screen, (124,252,0), game.snakeIcon)

    #Drawing Timer
    current_time = int((pygame.time.get_ticks() - game.initTime) / 1000)
    time = game.font.render("{}".format(current_time), True, (0,0,0))
    screen.blit(time, (390,25))

    #-----------------------------------------------
    
    # Update Screen
    pygame.display.flip()
    clock.tick(60)
    pygame.time.delay(50)