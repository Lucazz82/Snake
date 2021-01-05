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
    def __init__(self, row, column, index):
        self.rect = pygame.Rect(column * squareSize, (row * squareSize) + menuHeight, squareSize, squareSize)
        self.row = row
        self.column = column
        self.direction = "right"
        self.index = index
        self.nextDirection = []

    def changeDirection(self):
        if len(self.nextDirection) == 0:
            return
        
        if self.row == self.nextDirection[0][0] and self.column == self.nextDirection[0][1]:
            self.direction = self.nextDirection[0][2]
            self.nextDirection.pop(0)


class SnakeHead(SnakeBody):
    def __init__(self, row, column, index):
        SnakeBody.__init__(self, row, column, index)

    def changeDirection(self, direction):
        if direction in ["up", "down"] and self.direction in ["up", "down"]:
            return

        if direction in ["left", "right"] and self.direction in ["left", "right"]:
            return

        self.direction = direction

        pos = [self.row, self.column, direction]
        for square in snake.body:
            square.nextDirection.append(pos)

class Snake():
    def __init__(self):
        self.body = []

# Game Setup
snake = Snake()
snake.body.append(SnakeHead(5, 5, len(snake.body)))
# snake.body.append(SnakeBody(5, 4, len(snake.body)))
# snake.body.append(SnakeBody(5, 3, len(snake.body)))
# snake.body.append(SnakeBody(5, 2, len(snake.body)))
# snake.body.append(SnakeBody(5, 1, len(snake.body)))

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
                snake.body[0].changeDirection("up")
                pass
            if event.key == pygame.K_DOWN:
                snake.body[0].changeDirection("down")
                pass
            if event.key == pygame.K_LEFT:
                snake.body[0].changeDirection("left")
                pass
            if event.key == pygame.K_RIGHT:
                snake.body[0].changeDirection("right")
                pass

    # Snake movement
    movement()

    for square in snake.body[1:]:
        square.changeDirection()


    
    
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