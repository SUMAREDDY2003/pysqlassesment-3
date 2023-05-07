import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
z="insert into purchase values(%s,%s,%s)"
a=[(200,1000,"MyKids"),(201,1200,"ORay"),(202,3456,"vusfe"),(203,5000,"lion"),(204,7098,"King")]
cur.executemany(z,a)
mydb.commit()
print("Data inserted successfully")

