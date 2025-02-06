# while loop
i=0
while i<=5:
    print(i)
    i=i+1
# output: 0 1 2 3 4 5


i=1
sum=0
while i<=10:
    sum=sum+i
    i=i+1
print("sum = ",sum)
# output: sum = 55

i=1
while i <= 5:
    if i == 3:
        break
    print(i)
    i = i + 1
print("End of loop")

i=0
while i <= 5:
    i = i + 1
    if i == 3:
        continue
    print(i)

