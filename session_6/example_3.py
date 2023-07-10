#!/usr/bin/python

import mysql.connector

mysqldb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootpassword",
    database="python"
)
mycursor = mysqldb.cursor()

sql = "INSERT INTO route (id,network,mask,gateway) Values  (%s,%s,%s,%s)"
val = (1,"192.168.9.0","255.255.255.0","192.168.7.1")
mycursor.execute(sql,val)

mysqldb.commit()
