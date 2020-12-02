import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!",
  database="test002"
)
mycursor = mydb.cursor()

sql = "DELETE FROM customers  WHERE address LIKE '%Kostroma%'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount)