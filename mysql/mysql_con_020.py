import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!",
  database="test002"
)
mycursor = mydb.cursor()

sql = "DROP TABLE writers"

mycursor.execute(sql)