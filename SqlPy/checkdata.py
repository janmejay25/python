import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Janmejay@2005",
    database="fetcher"
)

cursor = conn.cursor()

attribute = input("Enter the attribute to find: ")
value = input("Enter the value to find: ")

# Validate attribute to prevent SQL injection (only allow specific columns)

   

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
