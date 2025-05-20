import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Janmejay@2005",
    database="college"
)

cursor = conn.cursor()

# 1️⃣ CREATE TABLE (if not exists)
create_table_query = """
    CREATE TABLE IF NOT EXISTS student (
        sr_no INT AUTO_INCREMENT PRIMARY KEY,
        enrollment_no VARCHAR(20) UNIQUE,
        name VARCHAR(100),
        course VARCHAR(100),
        birthdate DATE,
        contact_no VARCHAR(15)
    )
"""
cursor.execute(create_table_query)
print("Table 'student' created successfully!")

# 2️⃣ INSERT DATA (Using %s format)
insert_query = """
    INSERT INTO student (enrollment_no, name, course, birthdate, contact_no)
    VALUES (%s, %s, %s, %s, %s)
"""

student1 = ('2301031800059', 'Janmejay Pandya', 'CSE', '2005-05-02', '9512363057')
student2 = ('2301031800063', 'Malay Patel', 'CSE', '2004-05-18', '9512573636')
cursor.execute(insert_query, student1)
cursor.execute(insert_query, student2)
conn.commit()
print("New student inserted successfully!")

# 3️⃣ READ DATA (Retrieve)
cursor.execute("SELECT * FROM student")
print("\nStudent Records:")

for row in cursor.fetchall():
    print(row)

# Close the connection
cursor.close()
conn.close()
print("\nMySQL Connection Closed.")
