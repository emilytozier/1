import sqlite3
import os
import datetime

db_path='e://sqlite//'
db_file='db04.db'
full_path=os.path.join(db_path,db_file)


con=sqlite3.connect(full_path)

con.row_factory=sqlite3.Row

cur=con.cursor()
cur.execute('''
	SELECT * FROM books
	''')
#for i in cur.fetchall():
#	print(i)
	
#for i in cur.fetchall():
#	print(i['title_book'],i['author_book'])

for i in cur.fetchall():
	id_books, author_book, title_book, publish_book, age_book, keyword_book, value_book =i
	print(title_book,author_book)
