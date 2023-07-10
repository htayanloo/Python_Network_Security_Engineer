#!/usr/bin/python

import mysql.connector

mysqldb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootpassword"
)
mycursor = mysqldb.cursor()
mycursor.execute("CREATE DATABASE python")
mycursor.execute("show databases")
for x in mycursor:
    print(x)