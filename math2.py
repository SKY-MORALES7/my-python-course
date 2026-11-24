import math
print(math.pi)
print(math.e)

x = 9
result = math.sqrt(x)
print(result)

y = 9.1
result = math.ceil(y)
print(result)

z = 7.9
result = math.floor(z)
print(result)


#Excercise 1
#circumference of a circle

radius = float(input("Enter the radius of a circle?: " ))
circumference =  2 * math.pi * radius
print(f'The circumference is : {round(circumference, 2)}')

#Excercise 2
#Area of a circle

radius = float(input("Enter the radius of a circle?: "))
area = math.pi * pow(radius, 2)
print(f'The area of the circle is {round(area, 3)}cm\u00B2')


#Excercise 3 
#Find hypothenuse of a right angled triangle

a = float(input('Enter side A: '))
b = float(input('Enter side B: '))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'The hypothenuse of triangle with sides {a} and {b} is {c}')