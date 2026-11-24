name = input("Enter your full Name: ")
phone_number = input("Enter your Phone number: ")


# result = name.find(' ')
result = name.find('k')
result = name.rfind('k') #r means reverse so reversefind() gets the last occurence of what we are trying to find

name = name.capitalize() #this only capitalizes the first letter of a string because its one string 
print(name)

name = name.upper()
print(name)

name = name.lower()
print(name)

r = name.isdigit()
print(r)

r1 = phone_number.count('-')# the count method counts how may characters are contained in a string
print(r1)

r2 = name.isalpha()#Returns True only if characters are strings 
print(r2)


phone_number = phone_number.replace("-", ' ')
print(phone_number)

