square = lambda x : x * x

print(square(4))


# larger num
# num = lambda x, y : 
# print(num(5, 7))

people = [
    ("John", 20),
    ("Sarah", 18),
    ("Mike", 25)
]

people.sort(key=lambda people: people[1])

print(people)

# filter num

nums = [1, 2, 3, 4, 5, 6]
# filter(function, iterable)


nums = filter(lambda x: x % 2 == 0, nums)

print(list(nums))