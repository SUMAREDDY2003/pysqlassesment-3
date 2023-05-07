import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
t="create table goods(goods_id int primary key not null,man_date DATE,items_includes integer(30))"
cur.execute(t)