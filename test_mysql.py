import mysql.connector
from mysql.connector import Error

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ticket_universe",
        connection_timeout=5
    )
    if db.is_connected():
        print("MySQL connection successful!")
    else:
        print("Failed to connect")
except Error as e:
    print(f"Error: {e}")
finally:
    if db.is_connected():
        db.close()
