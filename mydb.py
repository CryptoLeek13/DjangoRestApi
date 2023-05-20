# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost", user="root", passwd="Blacksox13.")

# Prepare cursor object
cursorObject = dataBase.cursor()

# Creat db object
cursorObject.execute("CREATE DATABASE soxstream")

print("Database created!")
