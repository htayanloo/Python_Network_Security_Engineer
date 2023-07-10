#!/usr/bin/python

import mysql.connector

mysqldb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootpassword",
    database="python"
)
mycursor = mysqldb.cursor()

mycursor.execute("CREATE TABLE route (id INT,network VARCHAR(255),mask VARCHAR(255),gateway VARCHAR(255))")