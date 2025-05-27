import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Janmejay@2005",
    database="fetcher"
)

cursor = conn.cursor()


# 3️⃣ READ DATA (Retrieve)
cursor.execute("SELECT * FROM Birthdetails Where gender = 'M'")
print("\nStudent Records:")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()
