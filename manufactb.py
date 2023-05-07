import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Microsoft@2003",database="Inventory_Management")
cur=mydb.cursor()
t="create table manufacture(man_id integer(30),man_name varchar(30),man_comp varchar(30),no_of_items integer(30),defective integer(10))"
cur.execute(t)