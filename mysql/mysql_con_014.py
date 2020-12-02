import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!",
  database="test002"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")


myresult = mycursor.fetchone()

print(myresult)