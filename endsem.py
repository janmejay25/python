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

for i in range(2,20,2):
    print(i,end="")
    print()