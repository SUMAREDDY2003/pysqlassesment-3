import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
x="update manufacture set man_name='redtoys' where man_id=3"
cur.execute(x)
mydb.commit()