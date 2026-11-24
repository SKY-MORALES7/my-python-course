# Membership operators = used to test whether a value or variable is found in a sequence
#                        (strings, list,  'tuple', 'set', or 'dictionary')
#                        1. in
#                        2. not in


# STRINGS
# word = 'APPLE'

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f'There is a {letter}')
# else:
#     print(f'{letter} was not found')

# SETS

# students = {'spongebob', 'patrick', 'sandy'}

# student = input("Enter the name of a student: ")

# if student in students:
#     print(f'{student} is a student here')
# else:
#     print(f'{student} was not found')

# if student not in students:
    
#     print(f'{student} was not found')

# else:
#     print(f'{student} is a student here')

# DICTIONARIES
grades = {'Sandy': 'A', 
          'Squidward' : 'B', 
          'Spongebob' : 'C', 
          'Patrick': 'D'}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f'{student} was not found')


email = 'BroCode@gmail.com'

if '@' in email and '.' in email:
    print('Valid email')
else:
    print('Invalid email')


# LIST

fruits = ['apple', 'banana', 'orange']

user_input = input("Enter a fruit name: ")

if user_input in fruits:
    print(f'{user_input} exists')
else:
    print(f'{user_input} DNE')

    