import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
z="insert into manufacture values(%s,%s,%s,%s,%s)"
a=[(2,"shirt","Infosys",4,1),(1,"woodentable","SSEXport",2,0),(3,"red-colored-toys","wipro",6,0),(4,"wooden-chair","capgemini",10,0),(5,"jeans","SAP",20,0)]
cur.executemany(z,a)
mydb.commit()
print("Data inserted successfully")

