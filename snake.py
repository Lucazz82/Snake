import pygame
from sys import exit

# Pygame Setup
pygame.init()
clock = pygame.time.Clock()

# Display Setup
size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake By @Lucazz82")

# Grid Setup
menuHeight = 100
squareSize = 50

# Snake Setup

body = pygame.Rect(100,100, 50, 50)

while True:
    # Handling Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Background
    screen.fill((200,200,200))

    # Drawing The Grid
    for x in range(1, 16):
        pygame.draw.line(screen, (0,0,0), (squareSize * x, menuHeight), (squareSize * x, size[1]), 3)

    for y in range(10):
        pygame.draw.line(screen, (0,0,0), (0, menuHeight + y * squareSize), (size[0], menuHeight + y * squareSize), 3)
    
    body.x += 5

    # Drawing Snake
    pygame.draw.rect(screen, (124,252,0), body)

    # Update Screen
    pygame.display.flip()
    clock.tick(60)