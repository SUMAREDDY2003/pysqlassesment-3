import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
z="insert into goods values(%s,%s,%s)"
a=[(100,'01-04-23',4),(101,'01-04-23',2),(103,'01-05-23',10),(104,'28-04-23',10),(105,'28-04-23',10)]
cur.executemany(z,a)
mydb.commit()
print("Data inserted successfully")

