# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.
# Imports
import pygame
import random
import PYColor
from pygame.locals import*
import os

# img = pygame.image.load('/Users/ianthompson/Desktop/snowy_day/santassleigh.png')

class Screen:
    x = 1000
    y = 600

# Initialize game engine
pygame.init()


# Window
SIZE = (Screen.x, Screen.y)
TITLE = "Christmas Eve"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 30


def draw_cloud(x, y):
    pygame.draw.ellipse(screen, PYColor.cloudColor(), [x, y + 20, 40, 40])
    pygame.draw.ellipse(screen, PYColor.cloudColor(), [x + 60, y + 20, 40, 40])
    pygame.draw.ellipse(screen, PYColor.cloudColor(), [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, PYColor.cloudColor(), [x + 35, y, 50, 50])
    pygame.draw.rect(screen, PYColor.cloudColor(), [x + 20, y + 20, 60, 40])

def draw_bush(x, y):
    pygame.draw.ellipse(screen, PYColor.greenColor(), [x, y + 20, 40, 40])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [x, y + 20, 40, 40], 1)

    pygame.draw.ellipse(screen, PYColor.greenColor(), [x + 60, y + 20, 40, 40])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [x + 60, y + 20, 40, 40],1)

    pygame.draw.ellipse(screen, PYColor.greenColor(), [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [x + 20, y + 10, 25, 25],1)

    pygame.draw.ellipse(screen, PYColor.greenColor(), [x + 35, y, 50, 50])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [x + 35, y, 50, 50],1)

    pygame.draw.rect(screen, PYColor.greenColor(), [x + 20, y + 20, 65, 40])

def draw_light(x,y):
    pygame.draw.ellipse(screen, PYColor.randomLightColor(), [x, y, 10, 10])



''' make clouds '''
clouds = []
for i in range(25):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    clouds.append([x, y])

snow = []
for i in range(800):
    x = random.randrange(0, 1600)
    y = random.randrange(0, 800)
    r = random.randrange(1, 10)
    snow.append([x, y, r, r])

# Game loop
done = False
night = False

def santa():

    pygame.draw.rect(screen, PYColor.redColor(), [636, 80, 100, 50])

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
        elif event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
            print(event.pos)




    # Game logic
    ''' move clouds '''
    for c in clouds:
            c[0] -= 1
    if c[0] < -100:
        c[0] = random.randrange(800, 1600)
        c[1] = random.randrange(0, 200)
    for s in snow:
        s[1] += 6
    if s[1] > 700:
        s[0] = random.randrange(0, Screen.x)
        s[1] = random.randrange(0, Screen.x)

    # Drawing code

    ''' sky '''
    screen.fill(PYColor.blackColor())

    for s in snow:
        pygame.draw.ellipse(screen, PYColor.whiteColor(), s)

    ''' sun '''

    pygame.draw.ellipse(screen, PYColor.whiteColor(), [775, 75, 100, 100])

    ''' clouds '''
    for c in clouds:
        draw_cloud(c[0], c[1])


    ''' grass '''
    pygame.draw.rect(screen, PYColor.whiteColor(), [0, 400, Screen.x, 200])


    ''' fence '''
    y = 380
    for x in range(5, Screen.x, 30):
        pygame.draw.polygon(screen, PYColor.brownColor(), [[x+5, y], [x+10, y+5],
                                                [x+10, y+40], [x, y+40],
                                                [x, y+5]])
        pygame.draw.polygon(screen, PYColor.blackColor(), [[x+5, y], [x+10, y+5],
                                                [x+10, y+40], [x, y+40],
                                                [x, y+5]],3)

        pygame.draw.line(screen, PYColor.blackColor(), [0, 390-3], [Screen.x, 390-3], 3)
        pygame.draw.line(screen, PYColor.blackColor(), [0, 390+3], [Screen.x, 390+3], 3)
        pygame.draw.line(screen, PYColor.brownColor(), [0, 390], [Screen.x, 390], 5)

        pygame.draw.line(screen, PYColor.blackColor(), [0, 410+ 3], [Screen.x, 410+3], 3)
        pygame.draw.line(screen, PYColor.blackColor(), [0, 410- 3], [Screen.x, 410-3], 3)
        pygame.draw.line(screen, PYColor.brownColor(), [0, 410], [Screen.x, 410], 5)


    # screen.blit(img,(0,0))


    # House

    pygame.draw.polygon(screen, PYColor.houseColor(), [[204, 66+50], [30, 200+50], [390, 200+50]])
    pygame.draw.polygon(screen, PYColor.blackColor(), [[204, 66+50], [30, 200+50], [390, 200+50]],3)



    pygame.draw.rect(screen, PYColor.houseColor(), [60, 250, 300, 250])
    pygame.draw.rect(screen, PYColor.blackColor(), [60, 250, 300, 250], 3)

    pygame.draw.rect(screen, PYColor.darkBownColor(), [160, 370, 90,130])
    pygame.draw.rect(screen, PYColor.blackColor(), [160, 370, 90,130], 3)

    pygame.draw.rect(screen, PYColor.blueColor(), [260, 360, 90, 110])

    pygame.draw.polygon(screen, PYColor.greenColor(), [[349, 352+30], [349, 379+30], [334, 379+30]])
    pygame.draw.polygon(screen, PYColor.greenColor(), [[349, 369+30], [349, 399+30], [324, 399+30]])
    pygame.draw.polygon(screen, PYColor.greenColor(), [[349, 429-10], [349, 444], [315, 444]])
    pygame.draw.polygon(screen, PYColor.greenColor(), [[349, 429-5], [349, 444+25], [310, 444+25]])

    pygame.draw.rect(screen, PYColor.blackColor(), [305, 360, 5, 110])
    pygame.draw.line(screen, PYColor.blackColor(), [260, 412], [350, 412], 5)

    pygame.draw.rect(screen, PYColor.blackColor(), [260, 360, 90, 110],3)

    draw_bush(60, 450)
    draw_bush(280, 450)
    draw_light(89,475)
    draw_light(113,466)
    draw_light(137,482)
    draw_light(74,493)
    draw_light(110,496)
    draw_light(308,473)
    draw_light(296,489)
    draw_light(322,496)
    draw_light(360,494)
    draw_light(341,458)
    draw_light(319, 460)
    draw_light(341, 479)




    # Snowman
    pygame.draw.ellipse(screen, PYColor.whiteColor(), [785, 300, 80 , 80])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [785, 300, 80 , 80], 1)


    '''Nose'''
    pygame.draw.polygon(screen, PYColor.orangeColor(), [[800, 340], [830, 330], [830, 340]])


    pygame.draw.ellipse(screen, PYColor.blackColor(), [810 ,320, 10 , 10])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [830 ,320, 10 , 10])


    '''Mouth'''
    pygame.draw.ellipse(screen, PYColor.blackColor(), [800 ,340, 7 , 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [810 ,350, 7 , 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [820 ,352, 7 , 7])


    pygame.draw.ellipse(screen, PYColor.whiteColor(), [780, 360, 90 , 90])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [780, 360, 90 , 90], 1)
    pygame.draw.ellipse(screen, PYColor.whiteColor(), [775, 400, 100 , 100])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [775, 400, 100 , 100], 1)


# Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)
# Close window on quit
pygame.quit()
