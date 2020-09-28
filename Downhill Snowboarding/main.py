import pygame

# initialize pygame
pygame.init()

screen = pygame.display.set_mode((800, 700))

#

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # Checks to see if the user clicks the X in the window and if so, ends the loop
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()  # Needs to be added so the screen updates
