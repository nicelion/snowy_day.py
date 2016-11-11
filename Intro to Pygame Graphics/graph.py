# Imports
import pygame


# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "_____________________________________"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
WHITE = (255, 255, 255)
GRAY = (175, 175, 175)

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            

    # Drawing code
    screen.fill(WHITE)

    for x in range(0, 800, 20):
        pygame.draw.line(screen, GRAY, [x, 0], [x, 600], 1)

    for y in range(0, 600, 20):
        pygame.draw.line(screen, GRAY, [0, y], [800, y], 1)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
