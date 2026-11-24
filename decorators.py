# Decorators = A function that  extends the behaviour of another function without
#              Modifying the base function
#              pass the base function as an argument to the decorator

#              @add_sprinkles
#              get_ice_cream("Vanilla")

def add_sprinkles(func):
    def wrapper():
        print("You add sprinkles")
        func()
    return wrapper

def add_fugde(func):
    def wrapper():
        print("You add fudge")
        func()
    return wrapper

@add_sprinkles
@add_fugde
def get_ice_cream():
    print("Here is your ice cream")


get_ice_cream()



