# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains
#            It is a container for reusable values  
#strings
first_name = 'Bro'
food = "pizza"
email = 'bro123@fake.com'

print(first_name)


print(f"Hello {first_name}")
print(f'You like {food}')
print(f'Your email is {email}')

#integers
age = 25
quantity  = 3
num_of_students = 30

print(f'You are {age} years old')
print(f'You are buying {quantity} items')
print(f'Your class has {num_of_students} students')


#floats
price = 10.99
gpa = 3.2
distance = 5.5

print(f'The price is ${price}')
print(f'Your gpa is ${gpa}')
print(f'You  ran {distance}km')


#Boolean

is_student = False
for_sale = True
print(f'Are you a student?: {is_student}')

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is Not available")
