from itertools import product
from colorit import *
import mysql.connector

# Connecting to SQL Db
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Melon@123',
    database='python'
)
cursor = connection.cursor()

# CREATE
product_name = "Sponge"
product_price = 2.64

command = f'INSERT INTO python.sales(product_name, price)VALUES("{product_name}","{product_price}");'
cursor.execute(command)
connection.commit()  # used to DELETE, UPDATE or INSERT

# result = cursor.fetchall() # used for SELECT
# print(result)

cursor.close()
connection.close()

# READ

# UPDATE

# DELETE
