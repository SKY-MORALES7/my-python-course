# While loop = execute some code WHILE some condition remains true

# EXAMPLE 1
# name = input("Enter Your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter Your name: ")
# print(f"Hello {name}")

# EXAMPLE 2
# name = input("Enter Your name: ")

# while name == "":
#     print("You did not enter your name")
#     break
  
# print(f"Hello {name}")

# EXAMPLE 3
# age = int(input("Enter your age: "))

# while age < 0:
#     print("age can't be negative")
#     age = int(input("Enter your age: "))

# print(f'You are {age} years old')

# EXAMPLE 4
# food = input("Enter a food you like (q to quit)")

# while food != 'q':
#     print(f'You like {food}')
#     food = input("Enter another food that you like (q to quit): ")

# print("bye")

# EXAMPLE 5

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f'Your number is {num}')



