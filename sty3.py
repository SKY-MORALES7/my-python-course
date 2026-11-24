class Hero:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def Info(self):
        print(f"{self.name} is a superhero and is {self.age} years old")


class Cyclops(Hero):
    def __init__(self, name, age, power):
        super().__init__(name, age)
        self.power = power

    def Mutant_power(self):
            print(f"{self.name}'s super power is {self.power}")


class Wolverine(Hero):
    def __init__(self, name, age, behavior):
        super().__init__(name, age)
        self.behavior = behavior

    def trait(self):
        print(f"{self.name}  is {self.behavior}")


cyclops = Cyclops("Cyclops", 45, "Heat Vision")
wolverine = Wolverine("Wolverine", 78, "very very Agressive")
cyclops.Mutant_power()
cyclops.Info()
# cyclops.trait()
wolverine.trait()
wolverine.Info()

