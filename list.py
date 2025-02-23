column = ["name","age","phone"]
info1 = ["janmejay","20","9512363057"]
info2 = ["malay","21","9512573636"]

for column,info1,info2 in zip(column,info1,info2):
    print(column,"=",info1,",",info2)
print("")
# output: name = janmejay , malay
#         age = 20 , 21
#         phone = 9512363057 , 9512573636

# list concatination using (+) operator
li = []
for i in range(5):
    li.append(i)
x = list(li) + list(li) + [5,6,7,8]
print(x)
print("end of loop")
# output: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8]

#print the list using for loop
# for li in x:
#     print(li)
# print("end of loop")

# remove duplicates from list without function
li = [1,1,1,55,23,1,2,3,1,4,6,3,8,7,5,55,87,4,23,234]
clear_li = []
dup_li = []
for i in li:
    if i not in clear_li:
        clear_li.append(i)
print("duplicate removed",clear_li)
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] == li[j] and li[i] not in dup_li:
            dup_li.append(li[i])
print("duplicates are ",dup_li)
# print("duplicates are",dup_li)
# output: [1, 2, 3, 4, 6, 8, 7, 5, 55, 87, 23, 234]