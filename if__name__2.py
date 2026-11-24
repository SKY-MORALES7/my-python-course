# import if__name__
# print(__name__) # here __name__ will alwyas be equal to to the file name (in this case if__name__.py)
# print(if__name__.add(1 , 2))


import turtle

import math

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("white")


def  corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2  * n)-  2 * math.cos(3 * n)  - math.cos(4 * n)
    return x, y

t.penup()


for i in range(15):
    t.goto(0, 0)
    t.pendown()
    for n in range(0, 100, 2):
        x, y = corazon(n/ 10)
        t.goto(x * i, y * i)
    t.penup()

t.hideturtle()
turtle.done()



