# Logical Operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be true
#                     and = both conditions must be true
#                     not = inverts the condition (not False, not True)


# OR

temp = -5
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# AND

temp2 = 20
is_sunny = True

if temp2 >= 28 and is_sunny:
    print("It is HOT outside 🥵🥵")
    print("It is SUNNY 🌞")

elif temp2 <= 0 and is_sunny:
    print("It is COLD outside 🥶🥶")
    print("It is RAINY ☃️")

elif 28 > temp2 > 0 and is_sunny:
    print("It is WARM outside 🌞")
    print("It is just right 🐻")

# NOT

temp3 = 20
is_sunny = False

if temp3 >= 28 and  not is_sunny:
    print("It is HOT outside 🥵🥵")
    print("It is SUNNY 🌞")

elif temp3 <= 0 and not  is_sunny:
    print("It is COLD outside 🥶🥶")
    print("It is RAINY ☃️")

elif 28 > temp3 > 0 and not  is_sunny:
    print("It is WARM outside 🌞")
    print("It is just right 🐻")