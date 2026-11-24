import random

low = 1
high = 100
options = ('rock', 'paper', 'scissors')
cards = ['2', '3', '4', '5', '6', 'J', 'Q', 'K', 'A', '7']
# number = random.randint(low, high)
# number = random.random() #(this gives random number beween 0 and 1)
options = random.choice(options)
random.shuffle(cards)
print(cards)
print(options)