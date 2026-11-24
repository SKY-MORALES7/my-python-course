# multiple inheritance = inherit from more than one parent class 
#                        C(A, B)


# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A  [C= child, B = parent,  A = Grandparent]
#                          class C can inherit from B where  class B inherits from A

class Animal:
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

#prey and predator inherit from Animal class
class Prey(Animal):
    def flee(self):
        print("This animal is escaping")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")


# Rabbit hawk and fish inherit from prey/predator class which in turn inherit from Animal
class Rabbit(Prey):
    pass
    

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #multiple inheritance
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
fish.flee()
fish.hunt()
fish.sleep()

