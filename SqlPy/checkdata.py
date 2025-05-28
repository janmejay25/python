import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Janmejay@2005",
    database="fetcher"
)

cursor = conn.cursor()
attribute=input("enter the attribute to find: ")
value=input("enter the value to find: ")

query = f"SELECT * FROM Birthdetails WHERE {attribute} = {value!r}"
# 3️⃣ READ DATA (Retrieve)
cursor.execute(query)
print("\nStudent Records:")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()
