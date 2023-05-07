import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
t="create table sale(sale_id int primary key not null,sold_by varchar(30),profit int not null)"
cur.execute(t)