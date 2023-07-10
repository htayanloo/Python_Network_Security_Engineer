#!/usr/bin/python

import mysql.connector

mysqldb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootpassword",
    database="python"
)
mycursor = mysqldb.cursor()
mycursor.execute("UPDATE route set network='1.1.1.1'   where network='192.168.2.0'")

mysqldb.commit()
