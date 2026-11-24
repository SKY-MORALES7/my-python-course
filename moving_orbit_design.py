from turtle import *

import colorsys
import math


bgcolor("black")
tracer(0)
setup(700, 700)
hideturtle()
width(1)
num_points = 900
radius = 300
factor = 99


angle = [ 2 * math.pi * i / num_points for i in range(num_points)]

rotation_offset = 0

while True:
    clear()
    points = []

    for a in angle:
        x = radius* math.cos(a + rotation_offset)
        y = radius * math.sin(a + rotation_offset)
        points.append((x, y))

    for i in range(num_points):
        start_point = points[i]
        end_point = points[(factor * i) % num_points]
        hue = i / num_points
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        pencolor(rgb)
        penup()
        goto(start_point)
        pendown()
        goto(end_point)
    update()

    rotation_offset += 0.5