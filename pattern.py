word = "hello"
for i in range(1, len(word) + 1):
    print(word[:i])

rows = 6
for i in range(1, rows):
    print('+'*i)

# for loop z
for row in range(5):
    line = ""
    for col in range(5):
        if row == 0 or row+col==4 or row==4:
            line += "*"
        else:
            line += " "
    print(line)

# for lop a
for row in range(5):
    line = ""
    for col in range(5):
        if (row == 0) or (col==0)or( col==4)or(row==2):
            line += "*"
        else:
            line += " "
    print(line)


# for loop print G
for row in range(5):
    line = ""
    for col in range(5):
        if (row == 0  and col<4) or (col == 4 and row>1) or (col==2 and row>1) or (row==4 and col<3)or(row>0 and col==0):
            line += "*"
        else:
            line += " "