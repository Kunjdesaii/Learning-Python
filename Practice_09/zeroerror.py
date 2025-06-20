try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
except ZeroDivisionError:
    print("infinite")