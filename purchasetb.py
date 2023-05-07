import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
t="create table purchase(pur_id int primary key not null,pur_amount int,pur_by varchar(30))"
cur.execute(t)