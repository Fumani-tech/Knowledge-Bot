try:
    x=int(input("enter first number: ") )
    y=int(input("Second number: "))
    print(x/y)
except (ValueError, ZeroDivisionError):
    print("Something went wrong!")
