import mysql.connector
from dotenv import load_dotenv
import os

def get_db_connection():
    load_dotenv()
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )
    return conn

def populateFromCSV(csvPath, tableName):
    conn = get_db_connection()
    cursor = conn.cursor()
    with open(csvPath, "r") as file:
        cursor.execute("LOAD DATA LOCAL INFILE '" + csvPath + "' INTO TABLE " + tableName + " FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;")
    cursor.close()
    conn.close()

def createDatabase():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS " + os.getenv("DB_DATABASE"))
    cursor.close()
    conn.close()

def createTables():
    sqlPath = os.path.join(os.path.dirname(__file__), "tables.sql")
    conn = get_db_connection()
    cursor = conn.cursor()
    with open(sqlPath, "r") as file:
        cursor.execute(file.read())
    cursor.close()
    conn.close()

def createView():
    sqlPath = os.path.join(os.path.dirname(__file__), "views.sql")
    conn = get_db_connection()
    cursor = conn.cursor()
    with open(sqlPath, "r") as file:
        cursor.execute(file.read())
    cursor.close()
    conn.close()

def populateTables():
    armorCsv = os.path.join(os.path.dirname(__file__), "armor.csv")
    armorAdvCsv = os.path.join(os.path.dirname(__file__), "armorAdvance.csv")
    itemsCsv = os.path.join(os.path.dirname(__file__), "items.csv")
    itemsAdvCsv = os.path.join(os.path.dirname(__file__), "itemsAdvancement.csv")
    weaponsCsv = os.path.join(os.path.dirname(__file__), "weapons.csv")
    weaponsAdvCsv = os.path.join(os.path.dirname(__file__), "weaponsAdvance.csv")
    advCsv = os.path.join(os.path.dirname(__file__), "advancements.csv")
    populateFromCSV(armorCsv, "Armor")
    populateFromCSV(armorAdvCsv, "UnlocksArmor")
    populateFromCSV(itemsCsv, "Accessory")
    populateFromCSV(itemsAdvCsv, "UnlocksAccessory")
    populateFromCSV(weaponsCsv, "Weapon")
    populateFromCSV(weaponsAdvCsv, "UnlocksWeapon")
    populateFromCSV(advCsv, "Advancements")

def init():
    createDatabase()
    createTables()
    createView()
    populateTables()

if __name__ == "__main__":
    init()