# collection = single 'variable' used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set  = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

# LISTS


# fruits = ['apple', 'orange', 'banana', 'coconut']
# print(dir(fruits))


# print(fruits[2])
# print(fruits[0:3])
# print(fruits[::2]) #every second element beginning with index 0

# for x in fruits:
#     print(x)


# print(len(fruits))

# print('apple' in fruits)
# print('s' in fruits)
# fruits[0] = 'pineapple'

# for fruit in fruits:
#     print(fruit)


# fruits.append("apple")
# print(fruits)

# fruits.remove('apple')
# fruits.insert(0, 'pawpaw')
# # fruits.sort()
# # fruits.clear()
# print(fruits.index("pineapple"))

# print(fruits)

# SETS (we cant use index here cause sets are unordered e.g print(fruits[0]) gives subscriptable error cause sets are unordered)


# fruits = {'apple', 'orange', 'banana', 'coconut'}
# print(fruits) # notice that when this is printed it does not appear in the same order as the one on line 40
# fruits.add('pineapple')
# fruits.add('coconut')
# fruits.remove('orange')
# print(fruits)


# TUPLES

fruits = ('apple', 'orange', 'banana', 'coconut', 'coconut')

print(len(fruits))
print(fruits.index('apple'))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)


print(fruits)