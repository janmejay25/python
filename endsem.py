text = "silver oak university"
for letter in text:
    if letter == 'e':
        continue
    elif letter == 's':
        continue
    print(letter,end="")
print("\n")

print("method 2")
for letter2 in text:
    if letter2.lower() in ['e','s']:
        continue
    print(letter2,end="")
print("\n")

for i in range(1,20,2):
    print(i,end="")
    print()


# print("prime or not")
# num = int(input("Enter a number: ")) # Taking input fromthe user
# if num > 1:
#     for i in range(2, int(num ** 0.5) + 1): # Check divisibility upto√num
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#         else:
#             print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

