# FIltering = refers to the process of selecting elements
            # from an array that match a given condition

import numpy as np

ages  =  np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                   [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)] # & - and
adults = ages[(ages >= 18) | (ages < 65)] # | - or
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]



# print(adults)
print(evens)
print(odds)
print(seniors)
# print(teenagers)

adults = np.where(ages  >= 18, ages, 0) # where keeps original array whe making changes .where(condition, array, fillvalue), the fillvalue is the default value in the array that does not match condition set.
# Only use where when you need to preserve the original shape of your data





print(adults)