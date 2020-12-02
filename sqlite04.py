import sqlite3
import os
import datetime

db_path='e://sqlite//'
db_file='db04.db'
full_path=os.path.join(db_path,db_file)

#os.remove(full_path)

con=sqlite3.connect(full_path)
#cur=con.cursor()
#CREATE TABLE 
#CREATE TABLE IF NOT EXISTS
con.execute('''CREATE TABLE IF NOT EXISTS books(

 				id_books INTEGER PRIMARY KEY,
 				author_book TEXT,
 				title_book TEXT,
 				publish_book DATE,
 				age_book DATE,
 				keyword_book TEXT,
 				value_book REAL
 				)''')


for i in range(10):
	con.execute('''
		INSERT INTO books(id_books,author_book,title_book,publish_book,age_book) 
		VALUES (?,?,?,?,?)''',
		(i, "автор%s"%i, "заголовок%s"%i, datetime.date.today(), 
		datetime.date.today()+datetime.timedelta(days=i)))	
con.commit()
#cur.close()
con.close()