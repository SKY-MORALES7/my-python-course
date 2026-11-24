# Return statement = it is a statement used to end a function
#                    and send a result back to the caller

def add(x , y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    print(z)

def multiply(x, y):
    z = x * y
    return  z

def divide(x, y):
    z = x / y
    return z


subtract(1 , 2)

# print(add(1, 2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first +  ' ' + last

full_name = create_name("Bro", 'Code')
full_name = create_name("Spongebob", 'Sqarepants')

print(full_name)