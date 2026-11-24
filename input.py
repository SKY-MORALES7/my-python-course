#Input() =  A function tht prompts the user to enter data
#           Returns the entered data as a string

# name = input("What is your name?: ")
# age = int(input('How old are you?: ')) #we use int next to input cause age is an integer
# print(type(age)) # this is the check remove int and see what happens type becomes string and not integer
# print(f'Hello {name}') 
# print('Happy Birthday')
# print(f'You are {age} years old') 



# #Excercise 1:
# #Area of rectangle:
# length = float(input("Enter the length of the rectangle: "))
# width  = float(input("Enter the Width of the rectangle: "))
# Area = length * width
# print(f'The Area of the rectangle is {Area}cm\u00B2')


#Excercise 2:
#Shopping  cart program
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like to buy?: "))
total = price * quantity

if quantity > 1: 
    print(f"You bought {quantity} {item}s for a total of {total}")
else:
    print(f'You bought 1 {item} for a total of {total}')