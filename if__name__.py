# if __name__ == __main__: (this script can be imported OR run standalone)
#                           Functions and classes in this module can be reused
#                           Without the main block of code executing
#  Advantages: code is modular,
#              helps readability
#              leaves no global variables 
#              avoid unintended execution


# IT Allows us to run certain coded only if the file is run directly as a script 


# def add(x, y):
#     return x + y

# result = 'pass' if add(1, 2) == 3 else 'Fail'
# print(result)

# if __name__ == '__main__':
#     print()

# if we import the above as  module and run code in if__name__2.py like this the code above executes first before the code in the file we import it in. (i.e if__name__2.py) and we want the code for the file we import it in to run without our import executing or running first so we do this below(move everything to if__name == __main). it's much better when   if__name__.py file executes directly as a script(in it's own file) and not a module(import). Thats why we use if (dunder name) == '(dunder main)'

print(__name__) #this will always output __main__ as long as you called the if__name__ == '__main__' here
# Note : rnning the file with name == '__main__' (i.e the script file) always gives you dunder name = dunder main

def add(x, y):
  return x + y

if __name__ == '__main__':
    result = 'pass' if add(1, 2) == 3 else 'Fail'
    print(result)   

  
