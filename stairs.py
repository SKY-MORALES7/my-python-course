# def draw_stairs(n):
#     for i in range(n):
#         print(" " * i + "┐")

# draw_stairs(5)


def draw_stairs(n):
    length = n * 2 - 1
    for i in range(n):
        print(("*" * i).center(length))

draw_stairs(5)