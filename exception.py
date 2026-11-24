# Exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#              1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number: "))
    print(1/number)
# except ZeroDivisionError:
#     print("You can't divide by Zero, Idiot")
# except ValueError:
#     print("Enter only numbers please")
except Exception: #catches all exceptions(ZeroDivisionError, ValueError... etc) but is considered bad practice cause it does not tell user exact error
    print("SOmething went wrong")

finally:
    print("DO some clean up here")