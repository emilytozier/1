#Добавление описания автора
import sqlite3
import os
import datetime

db_path='c://Users//User//Desktop//json//'
db_file='db22.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()
sql='''\
	INSERT INTO author (name_author, descr_author)
	VALUES ("Чуковский", "Автор множества книг для детей")
	'''
cur.execute(sql)
con.commit()          # Завершаем транзакцию
cur.close()               # Закрываем объект-курсор
con.close()               # Закрываем соединение
 