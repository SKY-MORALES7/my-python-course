# For loops = execute a block of code a fixed number of times
#             You can iterate over a range, string, sequence, e.t.c

# for x in range(1, 11):
#     print(x)


# for x in reversed(range(1, 11)):
#     print(x)
# print("Happy new year")

#to count by 2 or in 2's add the  step note(start, end(exclusive), step)
# for x in range(1, 11, 2):
#     print(x)

# credit_card = '1234-5678-9012-3456'


# for x in credit_card:
#     print(x)


#we use the continue method to skip over an iteration
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

#we use the break method to well break out of an iteration
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)



