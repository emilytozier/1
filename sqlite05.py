import sqlite3
import os
import datetime

db_path='e://sqlite//'
db_file='db04.db'
full_path=os.path.join(db_path,db_file)


con=sqlite3.connect(full_path)

cur=con.cursor()
cur.execute('''
	SELECT * FROM books
	''')
for i in cur.fetchall():
	print(i)