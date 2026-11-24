#python calculator

operator = input("Enter an operator(+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f'Sum of {num1} and {num2} is : {round(result,2)}')
elif operator == '-':
    result = num1 - num2
    print(f'Difference of {num1} and {num2} is : {round(result, 2)}')
elif operator == "*":
    result = num1 * num2
    print(f'Product of {num1} and {num2} is : {round(result, 2 )}')
elif operator == '/':
    result = num1 / num2
    print(f'Quotient of {num1} and {num2} is : {round(result, 2)}')
else:
    print("Invalid Operator")
