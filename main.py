# yara's pygame homework
# 22.01.22

# import pygame package

import pygame

# define the variables:
LIGHT_CYAN = (224, 225, 225)
SKY_BLUE = (135, 206, 235)
PINK = (255, 20, 147)  # Pink. For the background color of your window
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ROYAL_BLUE = (65, 105, 225)
TOMATO = (255, 99, 71)
(WIDTH, HIGHT) = (600, 600)  # Dimension of the window

screen = pygame.display.set_mode((WIDTH, HIGHT))  # Making of the screen
pygame.display.set_caption('TUTORIAL 1, DONE BY YARA')  # Name for the window
screen.fill(SKY_BLUE)  # This syntax fills the background colour
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.draw.rect(screen, BLUE, [200, 100, 50, 20], width=0)
    pygame.draw.lines(screen, PINK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
    pygame.draw.ellipse(screen, (255, 0, 0), [225, 10, 50, 20], 2)
    pygame.draw.polygon(screen, (0, 255, 0), [[100, 100], [0, 200], [200, 200]], 5)
    pygame.draw.circle(screen, (65, 105, 225), [60, 250], 40)
    pygame.draw.arc(screen, TOMATO, [50, 50, 50, 50], start_angle=22 / 14, stop_angle=22 / 7, width=2)

    pygame.display.flip()

# end of code