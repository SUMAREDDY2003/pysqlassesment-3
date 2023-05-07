import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
z="insert into sale values(%s,%s,%s)"
a=[(10,"MyCare",1000),(11,"dontcare",2000),(12,"courage",5098),(13,"straightfor",1200),(14,"charitable",8764)]
cur.executemany(z,a)
mydb.commit()
print("Data inserted successfully")

