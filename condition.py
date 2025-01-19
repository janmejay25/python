#else if example
number = int(input("Enter a number: "))
if number > 0 :
    print("postive number")
elif number < 0 :
    print("negative number")
else :
    print("number is zero")

#nested if example
number2 = int(input("Enter a number2: "))
if number2 > 0 :
    if number2 == 5:
        print("number is 5")
    if number2 == 7:
        print("number is 7")
    print("postive number")
else:
    print("Number is zero")



