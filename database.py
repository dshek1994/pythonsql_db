import mysql.connector
from mysql.connector import Error
import pandas as pd

__pw__ = "password"

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("MySQL Database connection is successful")
    except Error as err:
        print("Error: '{err}'")
    
    return connection
    
connection = create_server_connection("localhost", "root", __pw__)