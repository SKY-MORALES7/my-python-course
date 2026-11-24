balance = 0
is_running = True





def show_balance(balance):
      print(f"--------------Your balance is ${balance:.2f}-------------")


def withdraw():
      amount = float(input("Enter amount to be withdrawn: "))

      if amount > balance:
            print("-----------------Insufficient funds----------------")
            return 0
        
      
      elif amount <= 0:
            print("-----------------amount must be greater than zero------------")
            return 0

      
      else:
            print(f"---------- ${amount} has been withdrawn ---------------")
            return amount

def deposit():
      amount = float(input("Enter amount  to be deposited: "))

      if amount <= 0:
            print("------------- amount must be greater than zero ----------------")
            return 0
            
      else:
            print(f" ------------ You have deposited ${amount:.2f} to Your account--------------")
            return amount

def main():
      pass


while is_running:
      print("Banking Program Online")
      print("choose an option below")
      print("1.Show Balance")
      print("2.Deposit")
      print("3.Withdraw") 
      print("4.Exit")

      choice = input("Enter your choice(1-4): ")


      if choice == "1":
            show_balance(balance)
      elif choice == "2":
            balance += deposit()
      elif choice == "3":
            balance -= withdraw()
      elif choice == "4":
            is_running = False
      else:
            print("-------------Enter a valid choice-----------")

print("--------<Thanks for your time, Hav a nice day>------------")
