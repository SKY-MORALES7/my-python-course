import numpy as np

array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])

# print(array.ndim)

# array[start: end : step]

# print(array[0:4:2])
# print(array[::2])

# print(array[:, 1]) #access columns
# print(array[:, 0:3]) #first three columns

# print(array[:, 1:4]) #skip first and contnue to last

# print(array[:, ::2]) #col 0 and col 2
# print(array[:, ::-1]) #reverse 

print(array[0:2, 0:2]) # first two rows of first two col 
print(array[0:2, 2:])
print(array[2:, 0:2])
print(array[2:, 2:])
