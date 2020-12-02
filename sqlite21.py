import sqlite3
import os
import datetime

db_path='g:/sqlite/'
db_file='db11.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)

#con=sqlite3.connect('/Users/dmitrijstennikov/SQLite/db11.db')
cur=con.cursor()




try:
	print(cur.execute('''
		SELECT * FROM books
		'''))
	print(cur.arraysize)
	print(cur.fetchall())
	print(cur.fetchall())

except sqlite3.DatabaseError as error:
	print(error)
else:
	print('Ok')

print(con.total_changes)
con.commit()
cur.close()
con.close()