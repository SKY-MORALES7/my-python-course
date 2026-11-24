# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own) 
#          useful to break up a large program reusable seperate files
# 
# 
# import math 
# import math as m
# from math import pi

# print(math.pi)
# print(m.pi)

# print(pi)

import module2

result = module2.pi
result2 = module2.square(3)
result3 = module2.cube(3)
result4 = module2.circumference(3)
result5 = module2.area(3)

print(result)
print(result2)
print(result3)
print(result4)
print(result5)