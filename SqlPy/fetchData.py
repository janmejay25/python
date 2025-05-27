import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Janmejay@2005",
    database="fetcher"
)

cursor = conn.cursor()


# 1️⃣ CREATE TABLE (if not exists)
create_table_query = """
    CREATE TABLE IF NOT EXISTS Birthdetails (
        sr_no INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        gender VARCHAR(10),
        birthdate DATE,
        birthtime VARCHAR(10),
        birthplace VARCHAR(100),
        contact_no VARCHAR(15)
    )
"""
cursor.execute(create_table_query)
print("Table 'Birthdetails' created successfully!")

# 2️⃣ INSERT DATA (Using %s format)
insert_query = """
    INSERT INTO Birthdetails (name, gender, birthdate, birthtime, birthplace, contact_no)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

jatak1 = ('Janmejay Pandya', 'M', '2005-05-02', '02:45', 'Mansa','9512363057')
jatak2 = ('malay patel', 'F', '2005-05-02', '02:45', 'Ahmedabad','9512573666')
cursor.execute(insert_query, jatak1)
cursor.execute(insert_query, jatak2)
conn.commit()
print("New jatak inserted successfully!")


# 3️⃣ READ DATA (Retrieve)
cursor.execute("SELECT * FROM Birthdetails Where gender = 'M'")
print("\nStudent Records:")
for row in cursor.fetchall():
    print(row)


    # Example DB operation (fetch all records)


# Close connection
cursor.close()
conn.close()
