import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anna",
  passwd="Sewerage23!",
  database="test002"
)
print(mydb)
cur=mydb.cursor()

cur.execute("SHOW TABLES")
for i in cur:
    print(i)