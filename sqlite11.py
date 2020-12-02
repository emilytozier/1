import sqlite3
import os
import datetime

db_path='g:/sqlite/'
db_file='db11.db'
full_path=os.path.join(db_path,db_file)

print(sqlite3.apilevel)
print(full_path)
con=sqlite3.connect(full_path)
con.close()
