import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
s="delete from manufacture where defective=1"
cur.execute(s)
mydb.commit()