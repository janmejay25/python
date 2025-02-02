vowel = "aeiouAEIOU"
text = input("Enter the text: ")

vowel_str = ""  # New string to store vowels
count = 0  # Counter for vowels

for char in text:
    if char in vowel:
        vowel_str += char  # Append vowel to string
        count += 1

print("Vowels:", vowel_str)
print("Count:", count)

