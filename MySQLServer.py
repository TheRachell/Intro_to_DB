import mysql.connector
from mysql.connector import Error 

def create_database():
    try:
        connection = mysql.connector.connect(
            host = 'localhost'
            user = 'Rachael'
            password = 'Paris567!'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXIST alx_book_store;")
            print("Database 'alx_book_store' created successfully")

    except Error as e:
        print (f"Error: {e}")

    finally: 
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "main":
    create_database()            
