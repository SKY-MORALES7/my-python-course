balance = 0
is_running = True

def show_balance(balance):
    print(f"---------Your Balance is {balance:.2f}-------------- ")
    return 0

def withdraw(balance):

    amount = float(input("Enter The amount you want to withdraw: "))


    if amount > balance:
        print("You are broke, you dont have that amount")
        return 0
    elif amount <= 0:
        print("Enter a valid amount please ")
        return 0
    else:
        print(f"You have withdraw {amount}")
        return amount
    

def deposit():
    amount = float(input("enter the amount you want to deposit: "))

    if amount <= 0:
        print("Enter a vid amount to deposit")
        return 0
    else:
        print(f"You have deposited {amount:.2f}")
        return amount


while is_running:
    print("Banking program online")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.withdraw")
    print("4.Exit")

    choice = int(input("Enter a choice (1- 4): "))

    if choice == 1:
        balance += show_balance(balance) 
    elif choice == 2:
        balance += deposit()
    elif choice == 3:
        balance -= withdraw(balance)
    elif choice == 4:
        is_running = False

    else: 
        print("Invalid choice")

print("Have a nice day")