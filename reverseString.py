string = input("Enter a string: ")

#reverse the string
# first the for loop will take each character one by one
# then it will add in rev and loop completes
# Example : string = "hello"
# char = h, rev = ""
# char = e, rev = h
# char = l, rev = eh
# char = l, rev = leh
# char = o, rev = lleh

rev = ""
for char in string:
    rev = char + rev
print("Reverse of the string is: ", rev)
if(string == rev):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")