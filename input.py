from datetime import datetime

current_yr = datetime.now().year
age = int(input("enter your age"))
if age >18 :
    print("you can vote ")
else :
    print("you can`t vote")
yr_age = 100+(current_yr -age)
print("your birth year is",2025-age)
print("100 yr completed in ",yr_age)
