tup = (2,"banana",5,9,8.5)
# give index of elemeent
print(tup.index("banana")) # 1
# count the elemt in the tuple
print(tup.count(2)) # 1 



# logical operators
print("logical operators")
a =10 
b =4
print (a and b) # 4
print (a or b) # 10
print (not b) # False

# bitwise operators
print("bitwise operators")
a = True
b = False
print (a & b) # False
print (a | b) # True
print (2 ^ 3) # 1
print (~1) # False
print(a>>b) # True
print(2<<2) # 8


j= 20
j= 10
print("hello world",j)


for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()


count = 1
while count <= 10:
    count += 1
    if count == 6:
        break 
    print(count)