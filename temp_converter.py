unit = input("Is this temperature in Celsius or Fahrenheit  (C/F)?: ").upper()
temp = float(input("Enter the temperature: "))

if unit == 'C':
    result = (9/5 * temp) + 32
    print(f'{temp} in {unit} is {round(result, 2)}F')

elif unit == "F":
    result = (temp - 32) *  5/9
    print(f'{temp} in {unit} is {round(result,2)}C')
    
else:
    print(f'{unit} is an invalid unit of measurement')
