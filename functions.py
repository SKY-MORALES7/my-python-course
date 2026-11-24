# function = A block of reusable code
#            place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old man!")
    print("Happy birthday to you!")
    print()

happy_birthday('Bro', 10)
happy_birthday('jake', 23)
happy_birthday('same', 45)
happy_birthday('jordan', 90)



def display_invoice(username, amount, due_date):
    print("---------Invoice---------")
    print(f'Hello {username}')
    print(f'Your bill of ${amount:.2f} is due: {due_date}')

display_invoice('Brocode', 42.50, '01/01/2025')


