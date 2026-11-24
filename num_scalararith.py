import numpy as np


# scalar arithmetic = a linear algebra term that means a single value

array = np.array([1, 2,3])

print(array + 1) #1 added to each value in the array
print(array - 2) #2 removed from each
print(array * 3)
print(array / 4)
print(array ** 5)

# Vectorized math functions = a vector is a single dimension such as a one d list

array = np.array([1.01, 2.5, 3.99])
print(np.sqrt(array))
print(np.floor(array))
print(np.pi)
# EXCERCISE

radii = np.array([1,2,3])

print(np.pi * radii ** 2)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2) #output = [5 7 9]
print(array1 - array2) #output = [-3 -3 -3]
print(array1 * array2) #output = [ 4 10 18]
print(array1 / array2) #output = [0.25 0.4  0.5 ]
print(array1 ** array2) #output = [  1  32 729]




