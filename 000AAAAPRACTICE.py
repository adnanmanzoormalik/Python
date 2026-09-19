try:
    amount = int(input("Enter amount: "))
    denom = int(input("Enter denom: "))
    print(amount/denom)

except ValueError:
    print("Enter correct value.")

except ZeroDivisionError:
    print("Cant divide by zero")