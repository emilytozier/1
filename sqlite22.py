import sqlite3
import os
import datetime

db_path='g:/sqlite/'
db_file='db11.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)

#con=sqlite3.connect('/Users/dmitrijstennikov/SQLite/db11.db')

con.row_factory=sqlite3.Row

cur=con.cursor()

try:
	print(cur.execute('''
		SELECT * FROM books
		'''))
	a_list=cur.fetchall()
	print(a_list)
	print(type(a_list))
	print(len(a_list))
	print(a_list[0][3])
	print(a_list[0]['title_book'])
	print(a_list[0]['TITLE_BOOK'])
	for i in a_list[0]:
		print(i)
	print(a_list[0].keys())

except sqlite3.DatabaseError as error:
	print(error)
else:
	print('Ok')

print(con.total_changes)
con.commit()
cur.close()
con.close()