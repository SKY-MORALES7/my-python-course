# from turtle import *


# import math


# speed(0)
# color('blue')
# bgcolor('white')

# def corazon(n):
#     x = 16 * math.sin(n) ** 3
#     y = 13 * math.cos(n) -  5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
#     return x, y

# penup()


# for i in range(15):
#     goto(0, 0)
#     pendown()
#     for n in range(0, 100, 2):
#         x, y = corazon(n/10)
#         goto(x* i, y * i)
#     penup()
# hideturtle()
# done()


def tree(height):
    length = 2 * height - 1
    stars = 1
    for i in range(height):
        print(('*' * stars).center(length))
        stars += 2
    print('*'.center(length))





if __name__ == "__main__":
    tree(9)
    print(__name__)




