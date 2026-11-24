# Variable scope = where a variable is visible and accessible
# Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# LOCAL 
def func1():
    a = 1
    print(a) #(local-scope) if this where b we have a Nameerror cause functions can't see inside other functions

def func2():
    b= 2
    print(b) # if this where a we have a Nameerror cause functions can't see inside other functioons

func1()
func2()

# ENCLOSED SCOPE 

def func1():
    x = 1

    def func2():
        x = 2
        print(x)
    func2()

func1()



# GLOBAL SCOPE
def func1():
    print(x)

def func2():
    print(x) 

x = 3

func1()
func2()


# BUILT_IN SCOPE
from math import e

def func1():
    print(e)

e = 4 
func1()
