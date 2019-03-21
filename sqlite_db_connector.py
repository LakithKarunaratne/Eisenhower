
import sqlite3

# open / create Database
conn = sqlite3.connect('test.db')

print("Open successfully")

# # create a table

conn.execute('''CREATE TABLE USER
             (ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT NOT NULL,
             ADDRESS CHAR(50),
             SALARY REAL);''')

print ("User Table Created")

conn.close()

# add values to the Table

conn.execute("INSERT INTO USER (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

conn.execute("INSERT INTO USER (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

conn.execute("INSERT INTO USER (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

conn.execute("INSERT INTO USER (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.commit()

print ("Records added successfully")

conn.close

# # SELECT OPERATION
conn = sqlite3.connect('test.db')

print("Opened successfully")

cursor = conn.execute("SELECT ID, NAME, ADDRESS, SALARY FROM USER")

for row in cursor:
      print ("ID = ", row[0])
      print ("Name = ", row[1])
      print ("Address = ", row[2])
      print ("Salary = ", row[3])
      print ('\n')

print('operation complete successfully')

# TODO: # SELECT ALL OPERATION

# cursor = conn.execute("SELECT * FROM USER")

# for i in cursor:
#       for k in i:
#             print (cursor[k])

# print('operation complete successfully')

# # # UPDATE OPERATION

# open / create Database
conn = sqlite3.connect('test.db')

print("Opened successfully")

conn.execute("UPDATE USER set SALARY = 25000.00 where ID= 1")
conn.commit()
print ("Total number of rows updated:",conn.total_changes)

cursor = conn.execute("SELECT id,name,address,salary FROM USER")
for row in cursor:
      print ("ID = ", row[0])
      print ("Name = ", row[1])
      print ("Address = ", row[2])
      print ("Salary = ", row[3])
      print ('\n')

print('operation complete successfully')

conn.close()
