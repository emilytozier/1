import sqlite3
import os
db_path='e://sqlite//'
db_file='db01.db'
full_path=os.path.join(db_path,db_file)
#print(full_path)

con=sqlite3.connect(full_path)
con.close()