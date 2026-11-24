# this i for print and return 
# print() → display something on the screen.
# return → send a value back to the caller.
# One fun fact

# If you might need the answer again, return it.
# If you just need to look at it once, print() it.

# Did you know that print() itself returns None?

# Try this:

x = print("Hello")
print(x)

def add_print(a, b):
    print(a + b)   # just displays it

def add_return(a, b):
    return a + b   # gives the value back

x = add_print(3, 4)   # prints "7" on screen
print(x)               # prints "None" !!

y = add_return(3, 4)  # nothing shown on screen
print(y)               # prints "7"

# print()
#  displays text to the console/screen. It doesn't give the value back to your program — it just shows it to a human.
# return
#  hands a value back to whatever called the function, so your program can use that value (store it, pass it to another function, do math with it, etc.)

# Every Python function returns something. If you never write a return statement (or write return with nothing after it), Python automatically returns None.
# python
def add_print(a, b):
    print(a + b)
    # no return here → function returns None automatically 

# So when you do x = add_print(3, 4), Python runs the function (which prints 7 as a side effect), and then hands back None to be stored in x, because that's literally all the function gave it.


def square(n):
    print(n * n)

result = square(5)   # screen shows: 25
total = result + 10  # ERROR — can't add None + 10

# You saw 25 on screen, so it feels like square(5) "is" 25 — but it isn't. It's None. The print was just a side effect.