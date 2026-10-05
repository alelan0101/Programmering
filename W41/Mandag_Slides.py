import sqlite3

conn = sqlite3.connect("animals.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM animals")

rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute("SELECT * FROM animals WHERE count > 20")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
