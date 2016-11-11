import pygame
from pygame.locals import *

SIZE = (640, 480)
pygame.init()
screen = pygame.display.set_mode(SIZE)
other1 = pygame.Surface([200, 200])

GREEN = (0, 255, 0)

done = False
screen.fill((0, 0, 0))
pygame.draw.rect(other1, GREEN, [0, 0, 50, 50])
other2 = pygame.transform.rotate(other1, 45)
screen.blit(other2, (0, 0))
pygame.display.flip()

while not done:
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break    
