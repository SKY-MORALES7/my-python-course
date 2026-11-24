# # these are one-dimensonal lists
# fruits =     ['apple', 'orange', 'banana', 'coconut']
# vegetables = ['celery', 'carrots', 'potatoes']
# meats =      ['chicken', 'fish', 'turkey']

# #two dimensional lists
# groceries = [fruits, vegetables, meats]

# print(groceries)
# print(groceries[0]) #returns fruits list
# print(groceries[1]) #returns vegetables list
# print(groceries[2])  #returns meats list


# print(groceries[2][0])



# or
groceries = [['apple', 'orange', 'banana', 'coconut'],
              ['celery', 'carrots', 'potatoes'],
                ['chicken', 'fish', 'turkey'],]

for collection in groceries:
    for food in collection:
        print(food)
    # print(collection)

# for collection in groceries:
#     for food in collection:
#         print(food, end = ' ')
#     print()