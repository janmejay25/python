import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="localhost",     # Change if needed
    user="root",          # Your MySQL username
    password="Janmejay@2005"  # Your MySQL password
)

cursor = conn.cursor()

# Create 'college' database
 
cursor.execute("CREATE DATABASE college")

# Check if 'college' database exists
cursor.execute("SHOW DATABASES")
databases = [db[0] for db in cursor.fetchall()]

if "college" in databases:
    print("Database 'college' has been created successfully!")
else:
    print("Database creation failed.")



# Close connection
cursor.close()
conn.close()
