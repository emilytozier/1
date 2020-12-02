import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!"
)

print(mydb)