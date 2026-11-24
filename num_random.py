import numpy as np


# random_number_generator = np.random.default_rng()
random_number_generator = np.random.default_rng(seed = 1)

print(random_number_generator.integers(low = 1, high = 7))
print(random_number_generator.integers(low = 1, high = 7, size = (3, 2))) #3 rows 2 colums


# floating points

print(np.random.uniform()) #generates a random floating point number between 0 and 1
print(np.random.uniform(low = -1, high = 1, size = 3)) 


# array shuffling
rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])

# fruits = rng.choice(fruits, size = 3)
fruits = rng.choice(fruits, size = (3, 3))

print(fruits)