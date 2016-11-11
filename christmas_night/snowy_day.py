## Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.
# Imports
import pygame
import random
import PYColor
import math
from pygame.locals import*
import os

# img = pygame.image.load('/Users/ianthompson/Desktop/snowy_day/santassleigh.png')

class Screen:
    x = 1000
    y = 600

class lightColor:


    colors = [PYColor.colorWithRGB(34, 204, 0), PYColor.rgb(225, 239, 31), PYColor.redColor()]






    #
    # for color in colors:
    #     if color[0] == color[]

    # list(set(colors))
    # a = []
    # for x in colors:
    #     if x not in a:
    #         c_1 = colors[0]
    #         c_2 = colors[1]
    #         c_3 = colors[2]
    #         a.append(x)
    #         print("if not called")
    #     else:
    #         colors[0] = PYColor.randomLightColor()
    #         colors[1] = PYColor.randomLightColor()
    #         colors[2] = PYColor.randomLightColor()
    #         print("else called")


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

def draw_smoke(x, y):
    pygame.draw.ellipse(screen, PYColor.whiteColor(), [x, y, 40, 60])
    pygame.draw.ellipse(screen, PYColor.whiteColor(), [x, y, 60, 40])
    pygame.draw.ellipse(screen, PYColor.whiteColor(), [x, y, 50, 50])




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

def draw_light(x,y,r, color):

    pygame.draw.ellipse(screen, color, [x, y, r, r])



''' make clouds '''
clouds = []
for i in range(25):
    x = random.randrange(-100, Screen.x)
    y = random.randrange(0,200)
    clouds.append([x, y])

smoke = []
for s in range(20):
    x = s * 50 + 150
    smoke.append(x)
    
snow = []
for n in range(1000):
    x = random.randrange(0, Screen.x)
    y = random.randrange(0, 800)
    r = random.randrange(1, 10)
    speed = random.randrange(1,4)
    snow.append([x, y, r, r])

# Game loop
done = False
night = False

def santa():

    pygame.draw.line(screen, PYColor.brownColor(), [707, 120],[691, 104],3)
    pygame.draw.line(screen, PYColor.brownColor(), [670, 105],[655, 119],3)
    pygame.draw.polygon(screen, PYColor.colorWithRGB(155, 12, 0), [[683,72], [671,80], [691, 81]])
    pygame.draw.ellipse(screen, PYColor.colorWithRGB(247, 217, 158), [675, 55, 20, 20])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [679, 62, 5, 5])
    pygame.draw.polygon(screen, PYColor.colorWithRGB(155, 12, 0), [[684, 40],[673, 57],[697, 57]])
    pygame.draw.ellipse(screen, PYColor.whiteColor(), [682, 37, 7, 7])
    pygame.draw.line(screen, PYColor.whiteColor(), [672, 56],[695, 56],3)
    pygame.draw.rect(screen, PYColor.redColor(), [636, 80, 90, 30])
    pygame.draw.line(screen, PYColor.brownColor(), [620,120],[737,120],3)
    pygame.draw.line(screen, PYColor.colorWithRGB(155, 12, 0), [669, 81],[667, 73], 5)

    # Reigndeer

    pygame.draw.ellipse(screen, PYColor.brownColor(), [500, 78, 20, 20])
    pygame.draw.line(screen, PYColor.brownColor(), [514, 89],[541, 103], 10)
    pygame.draw.line(screen, PYColor.brownColor(), [545, 108],[537, 125], 5)
    pygame.draw.line(screen, PYColor.brownColor(), [567, 112],[577, 125], 5)

    pygame.draw.rect(screen, PYColor.brownColor(), [531, 95, 50, 20])
    pygame.draw.ellipse(screen, PYColor.redColor(), [498, 87, 7, 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [507, 83, 5, 5])

    pygame.draw.line(screen, PYColor.colorWithRGB(109, 51, 0), [552, 99],[665, 73], 5)

def test(x):

    pygame.draw.ellipse(screen, PYColor.orangeColor(), [x + 526, 176, 100, 100])

lights_on = True

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
        elif event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
            print(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                lights_on = not lights_on




    # Game logic
    ''' move clouds '''
    for c in clouds:
            c[0] -= 1
    if c[0] < -100:
        c[0] = random.randrange(800, 1600)
        c[1] = random.randrange(0, 200)
    for s in snow:
        s[1] += 2

        if s[1] > 700:
            s[0] = random.randrange(0, Screen.x)
            s[1] = random.randrange(-200, 0)

    # Drawing code

    ''' sky '''
    screen.fill(PYColor.blackColor())

    smoke = [s + 1 if s < 800 else 150 for s in smoke]


    for s in smoke:
        x = s
        y = 15 *(0-1) * (math.sqrt(x - 25)) + 450
        
        pygame.draw.ellipse(screen, PYColor.whiteColor(), [x, y, 25, 25])
    if s == 850:
        x = s[2]

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

    santa()

    # screen.blit(img,(0,0))


    # House

    pygame.draw.rect(screen, PYColor.colorWithRGB(96, 35, 7), [300, 150, 50, 100])

    pygame.draw.polygon(screen, PYColor.houseColor(), [[204, 66+50], [30, 200+50], [390, 200+50]])
    pygame.draw.polygon(screen, PYColor.blackColor(), [[204, 66+50], [30, 200+50], [390, 200+50]],3)



    pygame.draw.rect(screen, PYColor.houseColor(), [60, 250, 300, 250])
    pygame.draw.rect(screen, PYColor.blackColor(), [60, 250, 300, 250], 3)

    '''Door'''
    pygame.draw.rect(screen, PYColor.darkBownColor(), [165, 370, 90,130])
    pygame.draw.rect(screen, PYColor.blackColor(), [165, 370, 90,130], 3)



    if lights_on:
        pygame.draw.rect(screen, PYColor.yellowColor(), [260, 360, 90, 110])
        pygame.draw.rect(screen, PYColor.yellowColor(), [70, 360, 90, 110])
    else:
        pygame.draw.rect(screen, PYColor.blueColor(), [260, 360, 90, 110])
        pygame.draw.rect(screen, PYColor.blueColor(), [70, 360, 90, 110])
        
    pygame.draw.polygon(screen, PYColor.greenColor(), [[349, 352+30], [349, 379+30], [334, 379+30]])
    pygame.draw.polygon(screen, PYColor.greenColor(), [[349, 369+30], [349, 399+30], [324, 399+30]])
    pygame.draw.polygon(screen, PYColor.greenColor(), [[349, 429-10], [349, 444], [315, 444]])
    pygame.draw.polygon(screen, PYColor.greenColor(), [[349, 429-5], [349, 444+25], [310, 444+25]])

    draw_light(343,397, 5, lightColor.colors[0])
    draw_light(331, 424, 5, lightColor.colors[1])
    draw_light(341, 421, 5, lightColor.colors[2])
    draw_light(341,431, 5, lightColor.colors[0])
    draw_light(326,441, 5, lightColor.colors[1])
    draw_light(344,449, 5, lightColor.colors[2])
    draw_light(334, 446, 5, lightColor.colors[0])
    draw_light(339, 407, 5, lightColor.colors[1])



    pygame.draw.rect(screen, PYColor.blackColor(), [305, 360, 5, 110])
    pygame.draw.line(screen, PYColor.blackColor(), [260, 412], [350, 412], 5)
    pygame.draw.rect(screen, PYColor.blackColor(), [113, 360, 5, 110])
    pygame.draw.line(screen, PYColor.blackColor(), [70, 412], [157, 412], 5)

    pygame.draw.rect(screen, PYColor.blackColor(), [260, 360, 90, 110],3)
    pygame.draw.rect(screen, PYColor.blackColor(), [70, 360, 90, 110],3)

    draw_bush(60, 450)
    draw_bush(280, 450)
    draw_light(89, 475, 10, lightColor.colors[0])
    draw_light(113, 466, 10, lightColor.colors[1])
    draw_light(137, 482, 10, lightColor.colors[2])
    draw_light(74, 493, 10, lightColor.colors[0])
    draw_light(110, 496, 10, lightColor.colors[1])
    draw_light(308, 473, 10, lightColor.colors[2])
    draw_light(296, 489, 10, lightColor.colors[0])
    draw_light(322, 496, 10, lightColor.colors[1])
    draw_light(360, 494, 10, lightColor.colors[2])
    draw_light(341, 458, 10, lightColor.colors[0])
    draw_light(319, 460, 10, lightColor.colors[1])
    draw_light(341, 479, 10, lightColor.colors[2])




    # Snowman
    pygame.draw.ellipse(screen, PYColor.whiteColor(), [785, 300, 80 , 80])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [785, 300, 80 , 80], 1)


    '''Nose'''
    pygame.draw.polygon(screen, PYColor.orangeColor(), [[800, 340], [830, 330], [830, 340]])


    pygame.draw.ellipse(screen, PYColor.blackColor(), [810,320, 10, 10])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [830,320, 10, 10])


    '''Mouth'''
    pygame.draw.ellipse(screen, PYColor.blackColor(), [800,340, 7, 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [810,350, 7, 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [820,352, 7, 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [833, 350, 7, 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [843, 342, 7, 7])

        
    pygame.draw.line(screen, PYColor.darkBownColor(), [795, 400], [750, 330], 10)
    pygame.draw.line(screen, PYColor.darkBownColor(), [853, 390], [897, 331], 10)

    pygame.draw.ellipse(screen, PYColor.whiteColor(), [780, 360, 90, 90])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [780, 360, 90, 90], 1)
    pygame.draw.ellipse(screen, PYColor.whiteColor(), [775, 400, 100, 100])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [775, 400, 100, 100], 1)



# Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)
# Close window on quit
pygame.quit()
