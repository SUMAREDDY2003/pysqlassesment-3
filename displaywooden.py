import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
f="select man_name from manufacture where man_name='wooden-chair'"
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)