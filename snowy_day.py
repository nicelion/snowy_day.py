## Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.
#
# Ian Thompson 256,97
# Imports
import pygame
import random
import PYColor
import math

class Screen:
    x = 1000  # screen width
    y = 600   # screen height

class lightColor:
    colors = [PYColor.colorWithRGB(34, 204, 0), PYColor.rgb(225, 239, 31), PYColor.redColor()]

# Initialize game engine
pygame.init()


# Window
SIZE = (Screen.x, Screen.y)
TITLE = "Christmas Eve"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

x1 = 300
santas_position = [635, 20]
santa_x = 635
nose_length = 800

lights_on = True
key_down_left = False
key_down_right = False
key_down_up = False
key_down_down = False
key_down_equals = False
key_down_minus = False

santas_sleigh = pygame.Surface([256, 100], pygame.SRCALPHA, 32)
mask=pygame.Surface((256,100),pygame.SRCALPHA)



presents = []

done = False
night = False
arms_up = True
ticks = 0



def draw_cloud(x, y):
    pygame.draw.ellipse(screen, PYColor.cloudColor(), [x, y + 20, 40, 40])
    pygame.draw.ellipse(screen, PYColor.cloudColor(), [x + 60, y + 20, 40, 40])
    pygame.draw.ellipse(screen, PYColor.cloudColor(), [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, PYColor.cloudColor(), [x + 35, y, 50, 50])
    pygame.draw.rect(screen, PYColor.cloudColor(), [x + 20, y + 20, 60, 40])

def draw_smoke():
    for s in smoke:
        x = s
        y = (17 *(0-1) * (math.sqrt(x)) + 450) - 15
        # y = (math.sqrt(x) * 50) + 450
        pygame.draw.ellipse(screen, PYColor.whiteColor(), [x, y, 25, 25])
        pygame.draw.ellipse(screen, PYColor.whiteColor(), [x - 5, y, 30, 20])

    if s == 850:
        x = s[2]

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
    x = s * 50 + 310
    smoke.append(x)

snow = []
for n in range(1000):
    x = random.randrange(0, Screen.x)
    y = random.randrange(0, 800)
    r = random.randrange(1, 10)
    speed = random.randrange(1,4)
    snow.append([x, y, r, r])

present = []
for n in range(1):
    x = santas_position[0]
    y = santas_position[1]
    present.append([x, y])

last_direction_left = True
def santa(x,y, frame, trans):


    red = (206, 41, 26, trans)
    dark_red = (86, 10, 0, trans)

    if frame == 0:
        red = (206, 41, 26, trans)
    elif frame == 1:
        red = dark_red


    if key_down_left or last_direction_left:

        pygame.draw.ellipse(santas_sleigh, (132, 11, 0), [190, 21, 45, 35])  # sack of toys
        pygame.draw.polygon(santas_sleigh, (132, 11, 0, trans), [[171, 33], [162, 45], [177, 45]]) # body
        pygame.draw.line(santas_sleigh, (132, 11, 0, trans), [162, 44], [156, 33], 3)  # arm

        pygame.draw.ellipse(santas_sleigh, (255, 219, 183, trans), [162, 15, 20, 20])  # santa's head
        pygame.draw.ellipse(santas_sleigh, (0,0,0, trans), [163, 22, 5, 5])  # santa's head
        pygame.draw.polygon(santas_sleigh, (237, 27, 0, trans), [[159, 18], [183, 18], [170, 5]])  # hat
        pygame.draw.ellipse(santas_sleigh, (255,255,255, trans), [169, 4, 5, 5]) # hat ball

        pygame.draw.line(santas_sleigh, (255,255,255, trans), [159, 18], [183, 18], 3)

        pygame.draw.line(santas_sleigh, (153, 98, 16, trans), [180, 75], [163, 94], 3)  # ski support
        pygame.draw.line(santas_sleigh, (153, 98, 16, trans), [206, 71], [227, 93], 3)  # ski support

        pygame.draw.rect(santas_sleigh, (206, 41, 26, trans), [148, 40, 90, 40])  # sleigh
        pygame.draw.line(santas_sleigh, (153, 98, 16, trans), [251, 94], [127, 94], 3)  # ski

        # reindeer

        pygame.draw.line(santas_sleigh, (112, 31, 0, trans), [20, 43], [24, 28], 3)  # antler
        pygame.draw.line(santas_sleigh, (112, 31, 0, trans), [24, 42], [30, 33], 3)  # antler
        pygame.draw.ellipse(santas_sleigh, (153, 98, 16, trans), [10, 40, 25, 25])  # head
        pygame.draw.rect(santas_sleigh, (153, 98, 16, trans), [35, 57, 70, 25])  # body
        pygame.draw.line(santas_sleigh, (153, 98, 16, trans), [40, 67], [22, 49], 13)  # neck
        pygame.draw.ellipse(santas_sleigh, red, [5, 50, 10, 10])  # nose
        pygame.draw.ellipse(santas_sleigh, (0,0,0, trans), [18, 45, 7, 7])  # nose
        pygame.draw.line(santas_sleigh, (112, 31, 0, trans), [69, 65], [156, 33], 3)  # leash

        pygame.draw.line(santas_sleigh, (153, 98, 16, trans), [45, 75], [39, 88], 3)  # leg
        pygame.draw.line(santas_sleigh, (153, 98, 16, trans), [55, 76], [47, 91], 3)  # leg
        pygame.draw.line(santas_sleigh, (153, 98, 16, trans), [82, 72], [95, 89], 3)  # leg
        pygame.draw.line(santas_sleigh, (153, 98, 16, trans), [80, 79], [88, 88], 3)  # leg

        screen.blit(santas_sleigh, (x, y))

        flipped = False



    if key_down_right or not last_direction_left:

        other2 = pygame.transform.flip(santas_sleigh, True, False)
        screen.blit(other2, (x, y))
    # if key_down_down and key_down_left:
    #
    #     other3 = pygame.transform.rotate(santas_sleigh, 5)
    #     screen.blit(other3, (x, y))





def draw_present(x,y):
    pygame.draw.rect(screen, PYColor.redColor(), [x, y + 15, 65, 50])
    pygame.draw.line(screen, PYColor.colorWithRGB(255,255,0), [x + 0, y + 41], [x + 63, y + 41], 10)  # ribbon
    pygame.draw.line(screen, PYColor.colorWithRGB(255,255,0), [x + 38, y + 14], [x + 38, y + 65], 10)  # ribbon
    pygame.draw.ellipse(screen, PYColor.colorWithRGB(255,255,0), [x + 30, y + 3, 12, 12])
    pygame.draw.polygon(screen, PYColor.colorWithRGB(255,255,0), [[x + 39, y + 8], [x + 53, y + 0], [x + 53, y + 11]])
    pygame.draw.polygon(screen, PYColor.colorWithRGB(255,255,0), [[x + 31, y + 8], [x + 16, y + 0], [x + 17, y + 12]])

# Game Loop

while not done:

    frame = ticks // 10

    ticks += 1

    if ticks >= 60:
        ticks = 0

    # Event processing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            print(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                lights_on = not lights_on
            if event.key == pygame.K_LEFT:
                key_down_left = True  # sets key_down bool to true
            if event.key == pygame.K_RIGHT:
                key_down_right = True
            if event.key == pygame.K_v:
                print(santas_position[0], santas_position[1])
            if event.key == pygame.K_a:
                arms_up = not arms_up
            if event.key == pygame.K_UP:
                key_down_up = True
            if event.key == pygame.K_DOWN:
                key_down_down = True
            if event.key == pygame.K_MINUS:
                key_down_minus = True
            if event.key == pygame.K_EQUALS:
                key_down_equals = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:  # left key has been un-clicked
                key_down_left = False
            if event.key == pygame.K_RIGHT:  # right key has been un-clicked
                key_down_right = False
            if event.key == pygame.K_UP:
                key_down_up = False
            if event.key == pygame.K_DOWN:
                key_down_down = False
            if event.key == pygame.K_MINUS:
                key_down_minus = False
            if event.key == pygame.K_EQUALS:
                key_down_equals = False

    if key_down_left:
        if santas_position[0] == -265:
            santas_position[0] = Screen.x + 10
        else:
            santas_position[0] -= 5
            last_direction_left = True
    if key_down_right:
        if santas_position[0] == 1100:
            santas_position[0] = -265
        else:
            santas_position[0] += 5
            last_direction_left = False
    if key_down_up:
        if santas_position[1] <= -10:
            santas_position[1] = santas_position[1]
        else:
            santas_position[1] -= 5
    if key_down_down:
        if santas_position[1] >= 290:
            santas_position[1] = santas_position[1]
        else:
            santas_position[1] += 5
    if key_down_minus:
        if nose_length >= 800:
            nose_length = nose_length
        else:
            nose_length += 5
    elif key_down_equals:
        if nose_length <= 365:
            nose_length = nose_length
        else:
            nose_length -= 5

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
    for p in present:
        p[1] += 2

        if p[1] > 354:
            p[0] = santas_position[0]
            p[1] = santas_position[1]
    # Drawing code

    # sky
    screen.fill(PYColor.blackColor())



    for s in snow:
        pygame.draw.ellipse(screen, PYColor.whiteColor(), s)

    # for p in present:
    #     draw_present(p[0] + 150, p[1])

    # sun
    pygame.draw.ellipse(screen, PYColor.whiteColor(), [775, 75, 100, 100])

    # clouds
    for c in clouds:
        draw_cloud(c[0], c[1])


    smoke = [s + 1 if s < 800 else 310 for s in smoke]


    draw_smoke()

    # grass
    pygame.draw.rect(screen, PYColor.whiteColor(), [0, 400, Screen.x, 200])


    # fence
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



    santa(santas_position[0], santas_position[1], frame, 255)

    # House

    pygame.draw.rect(screen, PYColor.colorWithRGB(96, 35, 7), [300, 150, 50, 100])

    pygame.draw.polygon(screen, PYColor.houseColor(), [[204, 66+50], [30, 200+50], [390, 200+50]])
    pygame.draw.polygon(screen, PYColor.blackColor(), [[204, 66+50], [30, 200+50], [390, 200+50]],3)



    pygame.draw.rect(screen, PYColor.houseColor(), [60, 250, 300, 250])
    pygame.draw.rect(screen, PYColor.blackColor(), [60, 250, 300, 250], 3)

    # door
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

    # nose
    pygame.draw.polygon(screen, PYColor.orangeColor(), [[nose_length, 340], [830, 330], [830, 340]])


    pygame.draw.ellipse(screen, PYColor.blackColor(), [810,320, 10, 10])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [830,320, 10, 10])


    # mouth
    pygame.draw.ellipse(screen, PYColor.blackColor(), [800,340, 7, 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [810,350, 7, 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [820,352, 7, 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [833, 350, 7, 7])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [843, 342, 7, 7])

    if arms_up:
        pygame.draw.line(screen, PYColor.darkBownColor(), [795, 400], [750, 330], 10)
        pygame.draw.line(screen, PYColor.darkBownColor(), [853, 390], [897, 331], 10)
    else:
        pygame.draw.line(screen, PYColor.darkBownColor(), [811, 372], [743, 424], 10)
        pygame.draw.line(screen, PYColor.darkBownColor(), [823, 375], [907, 421], 10)

    pygame.draw.ellipse(screen, PYColor.whiteColor(), [780, 360, 90, 90])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [780, 360, 90, 90], 1)
    pygame.draw.ellipse(screen, PYColor.whiteColor(), [775, 400, 100, 100])
    pygame.draw.ellipse(screen, PYColor.blackColor(), [775, 400, 100, 100], 1)



# Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)
# Close window on quit
pygame.quit()