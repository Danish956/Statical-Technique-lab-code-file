import sqlite3

conn = sqlite3.connect('StudentDetails.db')
print('Opened database Sucessfully')
query = """CREATE TABLE STUDENT_DETAILS ( ROLL_NO INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, 
AGE INT NOT NULL, ADDRESS CHAR(50))"""
conn.execute(query)
print("Table created successfully")

# Step-2: Inserting into a Table
query = """ INSERT INTO STUDENT_DETAILS(ROLL_NO, NAME, AGE, ADDRESS) VALUES (11212768, 'Shivam Kumar', 21, 
 'Bihar') """
conn.execute(query)
conn.commit()
print("Records created successfully")

# Step-3: Selection/Retrieve data from a Database
cursor = conn.execute("SELECT roll_no, name, address from STUDENT_DETAILS")
for row in cursor:
 print("ROLL NO = 11212768 ", row[0])
print("NAME = Shivam Kumar ", row[1])
print("ADDRESS = 21,'Bihar' ", row[2])
print("Operation done successfully")
conn.close()

# Step-4: Deletion from Table:
cursor = conn.execute("DELETE FROM STUDENT_DETAILS WHERE ROLL_NO = 11212768")
print("Record delete successfully")
conn.close()
