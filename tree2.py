
def tree(height):
    length = 2 * height - 1
    stars = 1

    for i in range(height):
        print(('*' * stars).center(length))
        stars += 2

    print('*'.center(length))

while True:
    user_input = input("Enter height (q to quit): ").lower()

    if user_input == "q":
        break

    tree(int(user_input))