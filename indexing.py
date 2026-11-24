# indexing = accessing elements of a sequence using [] (indexing operators)
#            [start(inclusive): end(exclusive): step]


credit_number = '1234-5678-9012-3456'

# print(credit_number[1])
print(credit_number[0:4]) #4 is exclusive
print(credit_number[5:9])
print(credit_number[10:14])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[-2])


print(credit_number[::2])  #step: this will print every second character in our string

last_digits = credit_number[-4:]
print(f'xxxx-xxxx-xxxx-{last_digits}')

# to reverse a string we set the step to be -1
credit_number  = credit_number[::-1]
print(credit_number)