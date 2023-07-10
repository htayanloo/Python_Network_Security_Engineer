#!/usr/bin/python

import mysql.connector

mysqldb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootpassword",
    database="python"
)
mycursor = mysqldb.cursor()
mycursor.execute("select * from route")

for x in mycursor:
    print(list(x))
