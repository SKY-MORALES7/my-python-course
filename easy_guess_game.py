import random
from colorama import Fore, Style
import pyfiglet
number_to_guess = random.randint(1, 100)

print(pyfiglet.figlet_format("Guessing Game", font = "Digital"))
# print(pyfiglet.FigletFont.getFonts())


while True:
    try:
        user_input = int(input("Enter a guess: "))

        if user_input < number_to_guess:
            print(Fore.RED  + f"{user_input} is too low, Try Again")
            print(Style.RESET_ALL + '')
        
        elif user_input > number_to_guess:
            print(Fore.MAGENTA + f"{user_input} is too High, try Again")
            print(Style.DIM + "")
        
        else:
            print( Fore.GREEN +  f"{user_input} is correct.You entered the right guess")
            print(Style.NORMAL + "Good job")
            print(Style.RESET_ALL + '')
            break
            
    except ValueError:
        print("Please enter a number")
        print(Style.BRIGHT + "")