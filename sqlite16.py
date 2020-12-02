#Замена и добавление в поле публикаций
import sqlite3
import os
import datetime

db_path='c://Users//User//Desktop//json//'
db_file='db22.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()




try:
	con.execute('''
		UPDATE publication SET name_publication='роман в стихах'
		WHERE id_publication = 3
		''')
	cur.execute ('''
		INSERT INTO publication (name_publication)
		VALUES ('поэма для детей')
		''')
except sqlite3.DatabaseError as error:
	print(error)
else:
	print('Ok')

print(con.total_changes)
con.commit()
cur.close()
con.close()