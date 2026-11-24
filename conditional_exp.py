# conditional expressions = A one-line shortcut for the if-else statement (ternary operator)
#                           print or assign one of two values based on a condition
#                           X if condition else Y

num = 20
a =  90
b = 6
temperature = 12
age = 19
user_role = 'admin4'

# print('Positive' if num > 0 else 'Negative')
# result = 'EVEN' if num % 2 == 0  else 'ODD'
# max_num = a if a > b else b
# min_num = a if a < b else b
# weather = 'HOT' if temperature > 20 else 'COLD (catch col..(vision joke))'
# status = 'Adult' if age >= 18 else 'Child'

access_level = "Full Access" if user_role == 'admin' else "Access denied"
# print(status)
# print(weather)
print(access_level)
# print(max_num)
# print(min_num)
