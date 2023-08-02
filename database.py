import mysql.connector
from mysql.connector import Error
import pandas as pd

__pw__ = "password"
#Function to create a server connection to database
def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database connection is successful")
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
    
connection = create_server_connection("localhost", "root", __pw__, "school")
create_database_query = "CREATE DATABASE school"
create_database(connection, create_database_query)