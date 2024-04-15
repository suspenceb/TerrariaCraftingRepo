import mysql.connector
from dotenv import load_dotenv
import os
import time

load_dotenv()

def get_db_connection():
    #Check if .env has port
    dbport = "3306"
    envPort = os.getenv("DB_PORT")
    if envPort is not None:
        dbport = envPort

    load_dotenv()
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE"),
        port=dbport
    )
    return conn

def init():
    # Check if the database is already created
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    cursor.close()
    conn.close()
    if len(tables) > 0:
        return
    
    # Create the database from the TerrariaDB.sql file
    conn = get_db_connection()
    cursor = conn.cursor()
    with open("TerrariaDB.sql", "r") as file:
        cursor.execute(file.read(), multi=True)
    try:
        conn.commit()
    except:
        print("Creating despite error")
    cursor.close()
    time.sleep(1)
    # Create views from views.sql
    conn2 = get_db_connection()
    cursor = conn2.cursor()
    with open("views.sql", "r") as file:
        cursor.execute(file.read(), multi=True)
    try:
        conn2.commit()
    except:
        print("Creating despite error")

if __name__ == "__main__":
    init()