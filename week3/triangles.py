# -*- coding: utf-8 -*-
import turtle
import random

QUIT_MSG = 'Press the "enter" key to quit the program.'

def pick_color():
    """Returns a random color string"""
    COLORS = ["blue","green","brown","red","goldenrod","gold", \
        "yellow","orange","turquoise","pink","purple","tan","deeppink",\
        "violet","forestgreen","darkorange"]
    random.shuffle(COLORS)
    return COLORS[0]

# define length of triangle and coordinates for lower left corner    
length = 50
x = -length/2
y = -length/2

# create pen of a random color
ran_color = pick_color()
pen = turtle.Turtle()
pen.color(ran_color)

# move pen to start position and prepare to draw
pen.penup()
pen.goto(x, y)
pen.pendown()

# draw a filled triangle of the given length
pen.begin_fill()
for i in range(3):
    print('Drawing line', i+1)
    pen.forward(length)
    pen.left(120)
pen.end_fill()

input(QUIT_MSG)

pen.clear()