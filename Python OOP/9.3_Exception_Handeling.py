try:

    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:

    print("Cannot divide by zero")

finally:

    print("Program finished")