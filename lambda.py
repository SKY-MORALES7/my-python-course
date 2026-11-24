# A lambda in Python is a way to create a small anonymous function (a function without a name).

# lambda parameters: expression

# For example:

# lambda x: x + 10

# means:

# def add_ten(x):
#     return x + 10

# Normally, you write a function like this:


# def square(x):
#     return x * x

# from rich import print
import pyfiglet
print(pyfiglet.figlet_format("LAMBDA.py", font = "future"))
# print(pyfiglet.FigletFont.getFonts())
from colorama import Fore, Style
square = lambda x: x * x

print( Fore.RED + str(square(5))) # can i use rich on non strings
print(Style.RESET_ALL + "")
students = [
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 72)
]

students.sort(key=lambda student: student[1]) # The lambda tells Python: "When sorting, use the second item (student[1]) as the key."

print(students)


# map()

# Transform every item in a list:

numbers = [1, 2, 3, 4]

squares = map(lambda x: x * x, numbers)

print(list(squares))

# filter()

# Keep only even numbers:

numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))

# Multiple Parameters
multiply = lambda x, y: x * y

print(multiply(3, 4))