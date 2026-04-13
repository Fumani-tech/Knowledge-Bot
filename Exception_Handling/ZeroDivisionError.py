try:
    a=int(input("Enter number: "))
    b=int(input("Enter divisor: "))
    print(a/b)
except ZeroDivisionError:
    print("You cannot divide by zero!")