# List comprehension  = A concise way to create  lists in python 
#                       Compact and easier to read than traditional loops
#                       [expression for  value in iterable if condition]

import math #this is for line 14 i could have done x * x but hey its good to know stuff

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

# Using list comp 
doubles = [x * 2 for x in range(1,11)]
triples = [y* 3 for y in range(1, 11)]
square = [round(math.pow(x, 2)) for x in range(1, 11)]

print(f'DOUBlED LIST: {doubles}')
print(f'TRIPLED LIST: {triples}')
print(f'SQUARED LIST: {square}')


fruits = ['apple', 'orange', 'banana', 'coconut']

fruits = [ fruit.upper() for fruit in fruits]

print(f'Fruits: {fruits}')

fruits = ['apple', 'orange', 'banana', 'coconut']

fruit_chars = [fruit[0] for fruit in fruits]

print(fruit_chars)



numbers = [-1, -2, 3, -4, 5, 6]
positive_nums =  [num for num  in numbers if num >= 0]
negative_nums =  [num for num  in numbers if num <  0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if not  num % 2 == 0]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)


grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)



