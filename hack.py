# import pyfiglet
# from colorama import Fore, Style, Back

# banner = pyfiglet.figlet_format("KENTER")

# print(Fore.CYAN + Back.GREEN + banner)
# print(Style.RESET_ALL + "")
import time
from colorama import Fore, Style
# from rich import print
from rich.console import Console
import pyfiglet
console = Console()

console.rule("Password Decrypter\n")

print(pyfiglet.figlet_format("Hacking...", font = "calvin_s"))


import time


password = "213"


for i in range(1000):
    guess  = str(i).zfill(3)
    time.sleep(0.02)
    print(Fore.RED + f"Hacking, Please Wait... {guess}", end = "")
    print(Style.RESET_ALL + "")

    if guess == password:
        print(Fore.BLUE + "password Found\n")
        print(Fore.GREEN + "Password is ", password)
        print(Style.RESET_ALL + "")
        break