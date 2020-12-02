import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!",
  database="test002"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)