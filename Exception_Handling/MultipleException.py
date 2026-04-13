try:
    x=int(input("Enter number: "))
    y=int(input("Enter divisor: "))
    print(x/y)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid input")