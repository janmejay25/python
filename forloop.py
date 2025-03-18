# 1. Iterating Over a Range
for i in range(5):
    print(i)
# Output: 0 1 2 3 4
# 7.9. Range with Start and Step
for i in range (2,9):
    print(i)
# output: 2 3 4 5 6 7 8
# 7.8. Reversed
for i in reversed(range(5)):
    print(i)
# output: 4 3 2 1 0
# 7.6. List Comprehensions
squares = [x**2 for x in range(5)]
print(squares)
# output: [0, 1, 4, 9, 16]

# 
# 6. Nested Loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
# output: (0, 0) (0, 1) (1, 0) (1, 1) (2, 0) (2, 1)
# nested loop in list comprehension
cartesian_product = [(x, y) for x in range(3) for y in range(2)]
print(cartesian_product)
# output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
# or
rows = 5
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print("*", end=" ")
    print()  # Move to the next line after each row
# output: 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 


# 3. Iterating Over a String
for char in "hello":
    print(char)
# output: h e l l o

# 2. Iterating Over a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple banana cherry

# 7.7. Enumerate
items = ["a", "b", "c"]
for index, item in enumerate(items):
    print(f" {index}: {item}")
# output: 0: a 1: b 2: c

# 6.1. Looping Over Multiple Lists
list1 = [1, 2]
list2 = ['A', 'B']
for num in list1:  # Outer loop
    for char in list2:  # Inner loop
        print(f"({num}, {char})")
#output: (1, A) (1, B) (2, A) (2, B)

# 7.5. Zip (Looping Over Multiple Lists)
names = ["Alice", "Bob"]
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# output: Alice: 85 Bob: 92

# Looping Over a List of Lists (Nested Lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:  # Outer loop for rows
    for item in row:  # Inner loop for elements in each row
        print(item, end=" ")
    print()  # New line after each row
#output:  1 2 3 
        #   4 5 6 
        #   7 8 9

# 4. Iterating Over a Tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)
# Output: red green blue

# 6.2. Looping Over a List of Tuples (Nested Tuples)
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"({x}, {y})")
# output: (1, 2) (3, 4) (5, 6)


# 6. Iterating Over a Set
my_set = {1, 2, 3}
for item in my_set:
    print(item)
# output: 1 2 3


# 5. Iterating Over a Dictionary
# Keys:
my_dict = {"name": "Ali", "age": 25}
for key in my_dict:
    print(key)
# Output: name age

# Values:
for value in my_dict.values():
  print(value)
# output: Ali 25

# Key-Value Pairs:
for key, value in my_dict.items():
   print(f"{key}: {value}")
# output: name: Ali age: 25

# 6.3. Looping Over a List of Dictionaries (Nested Dictionaries)
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
# output: name: Alice age: 25 name: Bob age: 30



# 10. Iterating With a Condition
for i in range(10):
    if i % 2 == 0:
        print(i)  # Prints even numbers
# output: 0 2 4 6 8


# 7. Loop Control Statements
# 7.1. Break
for i in range(10):
    if i == 5:
        break
    print(i)
# output: 0 1 2 3 4

# 7.2. Continue
for i in range(10):
    if i == 5:
        continue
    print(i)
# output: 0 1 2 3 4 6 7 8 9

# 7.3. Pass
for i in range(10):
    if i == 5:
        pass
    print(i)
# output: 0 1 2 3 4 5 6 7 8 9

# 7.4. Else
for i in range(10):
    print(i)
else:
    print("Done!")
# output: 0 1 2 3 4 5 6 7 8 9 Done!

