# class Restaurant:
#     def __init__(self):
#         self.menu = {
#             "Burger": 5000,
#             "pizza" : 8000,
#             "Coke" : 3000
#         }

#         self.orders = []

#     def show_menu(self):
#         print("\n___MENU___")
#         for item, price in self.menu.items():
#             print(f"{item} -- {price}")
       
#     def order(self, item):
#         if item in self.menu:
#             self.orders.append(item)
#             print(item, "added to cart")
#         else:
#             print("Item not available")

#     def bill(self):
#         total = 0
        
#         print("\n ___YOUR ORDER_____")
#         for item in self.orders:
#             print(item, "_", self.menu[item])
#             total += self.menu[item]

#         print("__________")
#         print("Total Bill: ", total)

# r = Restaurant()
# while True:
#     r.show_menu()
    
#     food = input("ënter food name: ")
#     r.order(food)

#     more = input("Order more food: (yes/no): ")
#     if more.lower() != "yes":
#         break

# r.bill()



def greet():
    return "name"
greet()

def greet():
    print("name")

greet() # returns only name cause we have not printed

def greet():
    print("name")
    return "nam"

y = greet()
print(y)