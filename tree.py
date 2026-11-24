def tree(height):
    length = height * 2 -1
    stars = 1
    for i in range(1, height + 1):
        print(('*' * stars).center(length))
        stars += 2
    print("*".center(length))

tree(9)






    

#     🌲 1. Your current version (classic & readable)
# def tree(height):
#     length = height * 2 - 1
#     stars = 1

#     for i in range(1, height + 1):
#         print(('*' * stars).center(length))
#         stars += 2

#     print("*".center(length))

# ✔ very readable
# ✔ easy to understand
# ✔ common in beginner code

# 🌲 2. Cleaner version (no extra variable stars)

# Most Python devs prefer this:

# def tree(height):
#     length = height * 2 - 1

#     for i in range(height):
#         stars = i * 2 + 1
#         print(('*' * stars).center(length))

#     print("*".center(length))
# 🧠 Why this is better

# Instead of tracking stars += 2, we calculate directly:

# row 0 → 1 star
# row 1 → 3 stars
# row 2 → 5 stars

# Formula:

# stars = i * 2 + 1
# 🌲 3. Super compact version (Pythonic)
# def tree(h):
#     for i in range(h):
#         print(('*' * (2*i + 1)).center(2*h - 1))
#     print('*'.center(2*h - 1))

# ✔ no extra variables
# ✔ math done inline
# ✔ very common in coding challenges

# 🌲 4. Return as a string (interview version)

# Instead of printing, build a result:

# def tree(height):
#     length = height * 2 - 1
#     result = []

#     for i in range(height):
#         stars = '*' * (2*i + 1)
#         result.append(stars.center(length))

#     result.append('*'.center(length))

#     return "\n".join(result)
# 🧠 Why this is important
# printing is for display
# returning string is for real applications/tests
# 🌲 5. One-liner (advanced / kata style)
# def tree(h):
#     return "\n".join(
#         ('*' * (2*i + 1)).center(2*h - 1)
#         for i in range(h)
#     ) + "\n" + '*'.center(2*h - 1)

# ✔ very compact
# ❌ harder to read
# ✔ common in Codewars solution
