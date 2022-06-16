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


def insert_command():
    product_name = "Sponge"
    product_price = 2.64

    command_insert = f'INSERT INTO python.sales(product_name, price)VALUES("{product_name}","{product_price}");'
    cursor.execute(command_insert)
    connection.commit()  # used to DELETE, UPDATE or INSERT
# insert_command()

# READ


def select_command():
    commandSelect = 'SELECT * FROM sales ORDER BY id_sale DESC'
    cursor.execute(commandSelect)
    result = cursor.fetchall()  # used for SELECT
    print(color("Select Query Executed!", Colors.purple))
    print(color(result, Colors.blue))
# select_command()

# UPDATE


def update_command():
    command_update = 'UPDATE sales SET product_name = "Avocado" where id_sale = "14"'
    cursor.execute(command_update)
    connection.commit()
    print(color("Update Query Execute!", Colors.yellow))
# update_command()

# DELETE


def delete_command():
    command_delete = 'DELETE FROM sales WHERE id_sale % 2 != 0'
    cursor.execute(command_delete)
    connection.commit()
    print(color("Update Query Execute!", Colors.red))


delete_command()

# Closes query
cursor.close()
connection.close()
