vowel = "aeiouAEIOU"
sum = 0
text=input("Enter the text: ")
for char in text:
    if char in vowel:
        print(char)
        sum+=1
print(sum)

