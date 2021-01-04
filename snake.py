import pygame
from sys import exit
from math import floor

# Functions ------------------------------------
def movement():
    for square in snake.body:
        if square.direction == "up":
            square.rect.y -= speed
            square.row -= 1
        elif square.direction == "down":
            square.rect.y += speed
            square.row += 1
        elif square.direction == "left":
            square.rect.x -= speed
            square.column -= 1
        elif square.direction == "right":
            square.rect.x += speed
            square.column += 1
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

# Snake Setup
squareSize = 20
speed = squareSize

class SnakeBody():
    def __init__(self, row, column, body):
        self.rect = pygame.Rect(column * squareSize, (row * squareSize) + menuHeight, squareSize, squareSize)
        self.row = row
        self.column = column
        self.direction = ""
        self.nextDirections = []
        self.behind = ""

    # def changeDirection(self):
    #     if len(self.nextDirections) == 0:
    #         return
        
    #     if self.nextDirections[0][0] in ["up", "down"]:
    #         if self.nextDirections[0][1] <= self.column:
    #             self.direction == self.nextDirections[0][0]
    #             self.nextDirections.pop(0)

    #     if self.row >= 6:
    #         self.direction = "up"
    def changeDirection(self, direction):
        if direction in ["up", "down"] and self.direction in ["up", "down"]:
            return

        if direction in ["left", "right"] and self.direction in ["left", "right"]:
            return

        self.direction = direction
        


class SnakeHead(SnakeBody):
    def __init__(self, x, y):
        SnakeBody.__init__(self, x, y)
        self.nextDirection = ""
        self.body = [self]

    def changeDirection(self, direction):
        if direction in ["up", "down"] and self.direction in ["up", "down"]:
            return

        if direction in ["left", "right"] and self.direction in ["left", "right"]:
            return

        self.direction = direction

        for square in self.body[1:]:
            square.nextDirections.append([direction, self.column])

class Snake():
    def __init__(self):
        self.snake = []

# Game Setup
# snake = SnakeHead(5, 5)
# snake.body.append(SnakeBody(5, 4))
snake = Snake()
snake.snake.append(SnakeBody(5, 5, ""))
snake.snake.append(SnakeBody(4, 5, snake.snake[-1]))

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
                snake.changeDirection("up")
                pass
            if event.key == pygame.K_DOWN:
                snake.changeDirection("down")
                pass
            if event.key == pygame.K_LEFT:
                snake.direction = "left"
                pass
            if event.key == pygame.K_RIGHT:
                snake.direction = "right"
                pass

    # Snake movement
    # body.updateColumn()
    # body.updateRow()
    # if body.column <= 3:
    #     speed = 0
    # changeDirection(isKeyDown)
    # if snake.nextDirection:
    #     snake.changeDirection()
    for square in snake.body[1:]:
        square.changeDirection()
        print(square.column)

    movement()

    # if snake.column >= 6:
    #     for square in snake.body:
    #         square.direction = "down"

    
    
    # Visuals --------------------------------------
    # Background
    screen.fill((200,200,200))

    # Drawing The Grid
    # for x in range(1, int(size[0] / squareSize)):
    #     pygame.draw.line(screen, (0,0,0), (squareSize * x, menuHeight), (squareSize * x, size[1]), 1)

    # for y in range(int(size[1] / squareSize)):
    #     pygame.draw.line(screen, (0,0,0), (0, menuHeight + y * squareSize), (size[0], menuHeight + y * squareSize), 1)
    
    # Drawing Snake
    for square in snake.body:
        pygame.draw.rect(screen, (124,252,0), square.rect)
    
    #-----------------------------------------------
    
    # Update Screen
    pygame.display.flip()
    clock.tick(15)