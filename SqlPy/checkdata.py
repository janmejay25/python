import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Janmejay@2005",
    database="fetcher"
)

cursor = conn.cursor()

# 2️⃣ INSERT DATA (Using %s format)
param_name = input("Enter name: ")
param_gender = input("enter Gender (M/F): ")
param_date = input("Enter birthdate (YYYY-MM-DD): ")
param_time = input("Enter birthtime (HH:MM): ")
param_place = input("Enter birthplace: ")
param_contact = input("Enter contact number: ")

insert_query = """
    INSERT INTO Birthdetails (name, gender, birthdate, birthtime, birthplace, contact_no)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
jatak = (param_name, param_gender, param_date, param_time, param_place,param_contact)




# fetch data based on user input
attribute = input("Enter the attribute to find: ")
value = input("Enter the value to find: ")

query1 = f"SELECT * FROM Birthdetails WHERE {attribute}"
query2 = f"= '{value}'"
query = query1 + query2
cursor.execute(query)

print("\nStudent Records:")
rows = cursor.fetchall()
if rows:
    for row in rows:
            print(row)
else:
        print("No records found.")

# Close connection
cursor.close()
conn.close()
