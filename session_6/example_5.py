#!/usr/bin/python

import mysql.connector

mysqldb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootpassword",
    database="python"
)
mycursor = mysqldb.cursor()
mycursor.execute("select * from route where network='192.168.0.0' and gateway='192.168.5.1'")

for x in mycursor:
    print(list(x))
