# create a 2d tuple since tuples are orderd and unchangeable and faster than lists

num_pad = ((1, 2, 3), 
           (4, 5, 6),
           (7, 8, 9),
           ('*', 0, '#'))


for row in num_pad:
    for num in row:
        print(num, end = ' ' )
    print()
