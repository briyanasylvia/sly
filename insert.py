import sqlite3
conn=sqlite3.connect('mitmorn.db')
print("open database successfully")
conn.execute("INSERT INTO Wanafunzi(ID,NAME, AGE, SCHOOL,GENDER)VALUES(1,'SYLVIA',19,'emobilis','female')")
conn.execute("INSERT INTO Wanafunzi(ID, NAME, AGE, SCHOOL, GENDER)VALUES (2,'joan',19,'emobilis','female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME, AGE, SCHOOL,GENDER)VALUES(3,'bivah',21,'emobilis','female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME, AGE, SCHOOL,GENDER)VALUES(4,'izoh',26,'emobilis','male')")

conn.commit()
print("records added successfully")
conn.close()