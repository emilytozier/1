import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!",
  database="test002"
)
mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Saint- Petersburg 123' WHERE address LIKE '%StPetersburg%'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount)