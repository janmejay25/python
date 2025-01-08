num1 = int((input("enter number ")))
num2 = int((input("enter number ")))
operation = input("enter operation ")
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("invalid operation")
