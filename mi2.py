
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

#prey and predator inherit from Animal class
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is escaping")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


# Rabbit hawk and fish inherit from prey/predator class which in turn inherit from Animal
class Rabbit(Prey):
    pass
    

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #multiple inheritance
    pass







rabbit = Rabbit('Bugs')
hawk = Hawk("mighty Eagle")
fish = Fish("Nemo")

rabbit.eat()
rabbit.sleep()
rabbit.flee() #because they inherit from prey class

hawk.eat()
hawk.sleep()
hawk.hunt() #because they inherit from predator class

fish.eat()
fish.sleep()

#fish inherits from predator and prey
fish.flee()
fish.hunt()