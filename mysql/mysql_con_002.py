import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE test002")
print(mycursor)