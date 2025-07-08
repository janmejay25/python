# 1. Check if a string contains only a-z, A-Z, and 0-9
def is_valid_string(s):
    for char in s:
        if not (char.isalnum()):  # Check if the character is not alphanumeric
            return False
    return True

# 2. Match a string with 'a' followed by zero or one 'b'
def match_a_b(s):
    return s == "a" or s == "ab"

# 3. Find sequences of lowercase letters joined by an underscore
def find_underscore_sequences(s):
    words = s.split()
    result = []
    for word in words:
        if "_" in word:
            parts = word.split("_")
            if all(part.islower() for part in parts):  # Check all parts are lowercase
                result.append(word)
    return result

# 4. Match a word containing 'z'
def word_with_z(s):
    words = s.split()
    return [word for word in words if 'z' in word]

# Example Usage

print(is_valid_string("Hello123"))  # True
print(match_a_b("ab"))  # True
print(find_underscore_sequences("hello_world test_case good_day"))  # ['hello_world', 'test_case']
print(word_with_z("amazing puzzle zoom"))  # ['amazing', 'puzzle', 'zoom']
