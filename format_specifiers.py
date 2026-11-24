# Format Specifiers = {value: flags} format a value based on what flags are inserted 
# 
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma operator
# modernize this hero section using cleaner Tailwind structure and improve responsiveness
price1 = 3.14159 
price2 = -987.65
price3 = 12.34
price4 = 30000.14637

# .2f displays to 2 decimal place
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

#for space
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

# To pad the space infront with a value
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:020}")

#To left justify a value
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

#To right justify a value (this is the actually the default way python renders a print)
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

#To center align
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

# To display a value with a plus sign (works only if number is positive)
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

#Or  just use a space

print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")

# With a comma(note this only works for values in the thousand place)
print(f"Price 4 is ${price4:,}")

# comma + .f 
print(f"Price 4 is ${price4:,.2f}")


# comma + .f + '+'
print(f"Price 4 is ${price4:+,.2f}")