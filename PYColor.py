# PYColor.py
# Ian Thompson
#
# Python lib that replicates the aspects of UIColor found in UIKit for iOS/MacOS
# 11/6/16

import random

def rgb(r,g,b):
        return (r,g,b)



def redColor():
    return (206, 41, 26)

def orangeColor():
    return (255, 155, 56)

def yellowColor():
    return (255, 255, 175)

def greenColor():
    return (0, 130, 23)

def skyBlueColor():
    return (75, 200, 255)

def blueColor():
    return rgb(9, 32, 68)


def brownColor():
    return (153, 98, 16)

def houseColor():
    return (145, 71, 37)

def blackColor():
    return  (0,0,0)

def whiteColor():
    return (255,255,255)

def darkBownColor():
    return (112, 31, 0)

def colorWithRGB(r,g,b):
    return (r,g,b)

def cloudColor():
    return (66, 66, 66)

def randomLightColor():

    c_1 = (206, 41, 26)
    c_2 = (34, 204, 0)
    c_3 = (225, 239, 31)

    return random.choice([c_1, c_2, c_3])
