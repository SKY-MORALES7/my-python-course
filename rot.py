def rotate_values(a, b, c):
    # Step 1: Save one of the values so it doesn't get wiped out
    temp = a
    
    # Step 2: Start overwriting
    a = c
 
    c = b
    b = temp

    # Step 3: Use the saved value to finish the rotation
    

    return a, b, c


print(rotate_values(1, 2, 3))


