column = ["name","age","phone"]
info1 = ["janmejay","20","9512363057"]
info2 = ["malay","21","9512573636"]

for column,info1,info2 in zip(column,info1,info2):
    print(column,"=",info1,",",info2)
# output: name = janmejay , malay
#         age = 20 , 21
#         phone = 9512363057 , 9512573636