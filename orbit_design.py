from turtle import *

import colorsys

import math


bgcolor("black")
tracer(2)
setup(700, 700)
width(1)
hideturtle()
points = []

for i in range(900):
    angle = 2 * math.pi * i /900
    x = 300 * math.cos(angle)
    y = 300 * math.sin(angle)
    points.append((x, y))
for i in range(900):
    start_point = points[i]
    end_point = points[(i * 99) % 900]
    hue = i / 99
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pencolor(rgb)
    penup()
    goto(start_point)
    pendown()
    goto(end_point)
update()

done()