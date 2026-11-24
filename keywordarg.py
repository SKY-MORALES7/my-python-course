# keyword arguments  = an argument preceded by an identifier
#                      helps with readability
#                      order of arguments doesn't matter     
#                      1.positional 2.default 3.keyword 4.arbitrary


def hello(greeting, title, first, last):
    print(f'{greeting} {title} {first} {last}')

hello("Hello", 'Mr', 'Spongebob', 'Sqaurepants')
hello("Hello", 'Spongebob', 'Sqaurepants', 'Mr' )
hello("Hello", title = 'Mr', first = 'Spongebob', last = 'Sqaurepants' )
hello("Hello", title = 'Mr',  last = 'Sqaurepants', first = 'Spongebob' )

# make sure positonal arguments are first (in this case i.e is 'Hello'(positional arg) and title, last , first are keyword arguments so if i were to have)
# hello( title = 'Mr',  last = 'Sqaurepants', first = 'Spongebob', "Hello")
# i'd get a  SyntaxError: positional argument follows keyword argument

for x in range(1, 11):
    print(x, end = " ") #funfact end is a keyword argument found within the print statement

print('1', '2', '3', '4', '5', sep = '-') #another is sep

def get_phone(country, area, first, last):
    return f'{country}-{area}-{first}-{last}'

phone_num = get_phone(country = 1 , area = 123 , first =456 , last =7890 ,)
print(phone_num)