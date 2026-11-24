#  *args   = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1.positonal 2. default 3.keyword 4.ARBITRARY

# type(args) = tuple()
# type(kwargs) = dictionary{}

# def add(a, b):
#     return a + b

# print(add(1, 2, 3))# ths gives error cause our function takes two positonal arguments but this has three

def employer(*args):
    # for arg in args:
    #     print(arg)
        print(f"Your name is {args[0]}, You live on {args[2]} and you are {args[1]} years old.")


employer("jake", 10, "Gnassingbe Eyadema street")

def add(*args):
    # print(type(args))
    total = 0
    for arg in args:
        total  += arg
    return total



# add(1, 2, 3)
print(add(1, 2, 3, 4,5 ))


def display_name(*args):
    for arg in args:
        print(arg, end = " ")

display_name("DR", "Spongebob", 'Harold', "Squarepants", "III")

# kwargs

def print_address(**kwargs):
   
#    for value in kwargs.values():
#     print(value)

#    for key in kwargs.keys():
#     print(key)

     for key, value in kwargs.items():
        print(f'{key} : {value}')


print_address(street = '123 Fake St',
              apt = '100',
              city = 'Detroit', 
              state = 'MI' , 
              zipcode = "54321" , )
              
             
# using args & kwargs together
# Remember kwargs most follow args so meaning args always comes first

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = '')
    print()

    if 'apt' in kwargs:
        
        print(f"{kwargs.get('street')}  {kwargs.get('apt')}")

    else:
        print(f'{kwargs.get('street')}') 


    # for value in kwargs.values():
    #     print(value, end = ' ')

    print(f"{kwargs.get('city')} - {kwargs.get('state')} - {kwargs.get('zip')} ")

shipping_label('Dr', 'Spongebob', 'Squarepants', 'III',
                street = '1234 Fake st.',
                apt = '1000',
                city = 'Detroit',
                state = 'MI',
                zip = '54321')




