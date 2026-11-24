# Aggregate functions = summarize data and typically return a single value

import numpy as np

array = np.array([[1 , 2, 3, 4, 5],
                  [6 , 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array)) #standard deviation
print(np.var(array)) #Variance(square of standard deviation)
print(np.min(array)) #minumum value
print(np.max(array)) #max value
print(np.argmin(array)) # position of minimum value
print(np.argmax(array)) # position of max value

print(np.sum(array, axis = 0)) # apply this to all columns
print(np.sum(array, axis = 1)) # apply this to all rows