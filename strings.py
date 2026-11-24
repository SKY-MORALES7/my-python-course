name = input("Enter your full Name: ")

result = str(len(name)) #I change this int type to string so i can concatenate it with letters to have (number) letters

print(f'Hello, my name is {name} and it has ', result + " letters")


print(type(len(name)))
print(type(str(len(name))))


