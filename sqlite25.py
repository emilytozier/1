import sqlite3
import os
import datetime

db_path='g:/sqlite/'
db_file='db11.db'
full_path=os.path.join(db_path,db_file)

#con=sqlite3.connect("/Users/dmitrijstennikov/SQLite/db11.db")
con=sqlite3.connect(full_path)
cur=con.cursor()

var1=("Маршак",)
sql1='''INSERT INTO author (name_author) VALUES(?)'''


try:
	cur.execute(sql1,var1)
	cur.execute("SELECT * FROM author")
	print(cur.fetchall())

	con.rollback()
	cur.execute("SELECT * FROM author")
	print(cur.fetchall())

except sqlite3.DatabaseError as error:
	print(error)
else:
	print('Ok')
con.commit()
cur.close()
con.close()


