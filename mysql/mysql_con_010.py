import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!",
  database="test002"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Sergey Esenin', 'Moskow 4'),
  ('Petr Shedrin', 'StPetersburg 652'),
  ('Marina Cvetaeva', 'Moskow 21'),
  ('Anna Ahmatova', 'StPetersburg 345'),
  ('Vladimir Mayakovskiy', 'Moskow 2'),
 
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount)