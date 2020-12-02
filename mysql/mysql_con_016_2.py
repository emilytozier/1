import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!",
  database="test002"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address= %s"
val=('StPetersburg',)
mycursor.execute(sql,val)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)