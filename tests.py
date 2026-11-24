# is_running = True

# def evenOdd():
#     result = input('Enter a number (press q to quit): ').lower()

#     if result == 'q':
#         return 'q'

#     num_result = float(result)

#     if num_result % 2 == 0:
#         return True
#     else:
#         return False

# while is_running:
#     answer = evenOdd()


#     if answer == "q":
#         is_running = False
#     else:
#         print(answer)
# 

# name = "orange"

# if type(name) == str:
#     print(True)
# else:
#     print(False)

# x = 890.0
# print(type(x))

# def tree(height):
#     length = height * 2 -1
#     stars = 1

#     for i in range(1, height + 1):
#         print(('*' * stars).center(length))
#         stars += 2
#     print('*'.center(length))

# tree(11)
def tree(height):
    length = height * 2 -1
    stars = 1

    for i in range(height):
        print(('*' * stars).center(length))
        stars += 2
    print('*'.center(length))

while True:
    user_input = input('Enter a desired tree Christmas height(enter q to quit): ').lower()


    if user_input == 'q':
        break
    
    tree(int(user_input))



import test2

print('test3 says',  __name__)