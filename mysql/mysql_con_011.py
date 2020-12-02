import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!",
  database="test002"
)
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Alexande Block", "StPetersburg")
mycursor.execute(sql, val)

mydb.commit()

print( mycursor.lastrowid)