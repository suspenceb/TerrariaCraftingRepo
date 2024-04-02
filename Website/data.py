import mysql.connector
from dotenv import load_dotenv
import os
import hashlib

# ----------------- Begin Helper Functions ----------------- #

def get_db_connection():
    load_dotenv()
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )
    return conn

# ------------------ End Helper Functions ------------------ #

# --------------------- Begin Endpoints -------------------- #


# Post Login Function - Use this to log in a user
# Inputs: username (string), password (string)
# Outputs: token (string) or None
def post_login(username, password):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Query the database
    query = "SELECT UserId, Username FROM Account WHERE Username = %s AND PasswordHash = %s"
    cursor.execute(query, (username, hashed_password))
    
    # If a user is not returned, return None
    user = cursor.fetchone()
    if user is None:
        return None
    
    # Generate a token for the user and post it to the database
    token = hashlib.sha256(os.urandom(64)).hexdigest()
    query = "INSERT INTO UserSession (UserId, Token) VALUES (%s, %s)"
    print(str(user[0]) + " " + str(token))
    cursor.execute(query, (str(user[0]), str(token)))
    conn.commit()

    # Close the connection and return the token
    conn.close()
    return token


# Delete Login Function - Use this to log out a user
# Inputs: token (string)
# Outputs: True if successful, False if not
def delete_login(token):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Ensure the token exists
    query = "SELECT Token FROM UserSession WHERE Token = %s"
    cursor.execute(query, (token, ))
    if cursor.fetchone() is None:
        return False

    # Query the database
    query = "DELETE FROM UserSession WHERE Token = %s"
    cursor.execute(query, (token, ))
    conn.commit()

    # Close the connection and return 1 if successful
    conn.close()
    return True


# Gets the current logged in uses from the token. Returns dictionary with user id and username.
# Returns None if the token does not exist in the datebase
def get_loggedin_user(token) -> dict:

    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Ensure the token exists
    query = "SELECT UserId FROM UserSession WHERE Token = %s"
    cursor.execute(query, (token, ))
    userid = cursor.fetchone()[0]
    if userid is None:
        return None

    query = "SELECT Username FROM Account WHERE UserId = %s"
    cursor.execute(query, (userid, ))
    username = cursor.fetchone()[0]

    user = {
        "userId": userid,
        "username": username
    }

    # Close the connection and return the user id
    conn.close()
    return user 


def update_password(userId, password):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Query the database
    query = "UPDATE Account SET PasswordHash = %s WHERE UserId = %s"
    cursor.execute(query, (hashed_password, userId))
    conn.commit()

    # Close the connection and return 1 if successful
    conn.close()
    return True


def get_characters(userId):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database
    query = "SELECT CharId, CharName, WeaponId FROM TerrariaCharacter WHERE UserId = %s"
    cursor.execute(query, (userId, ))
    characters = cursor.fetchall()

    # Close the connection and return the characters
    conn.close()
    returnCharacters = []
    for i in characters:
        returnCharacters.append({
            "charId": i[0],
            "charName": i[1],
            "weaponId": i[2]
        })
    return returnCharacters

def add_character(userId, charName):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database
    query = "INSERT INTO TerrariaCharacter (UserId, CharName) VALUES (%s, %s)"
    cursor.execute(query, (userId, charName))
    conn.commit()

    # Close the connection and return 1 if successful
    conn.close()
    return True

def delete_character(charId):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database
    query = "DELETE FROM TerrariaCharacter WHERE CharId = %s"
    cursor.execute(query, (charId, ))
    conn.commit()

    # Close the connection and return 1 if successful
    conn.close()
    return True

# Function takes in list of advancement ID's
def get_items(advancements):
    accessoryReqs = {}
    armorReqs = {}
    weaponReqs = {}

    # Get all accessory requirements, armor requirements, and weapon requirements
    # Store in accessoryReqs, armorReqs, and weaponReqs respectively
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM UnlocksAccessory"
    cursor.execute(query)
    accessoryRequirements = cursor.fetchall()
    for req in accessoryRequirements:
        accessoryId = req[1]
        advancementId = req[0]
        # Check if the accessory is already in accessoryReqs
        if accessoryId in accessoryReqs:
            accessoryReqs[accessoryId].append(advancementId)
        else:
            accessoryReqs[accessoryId] = [advancementId]

    query = "SELECT * FROM UnlocksArmor"
    cursor.execute(query)
    armorRequirements = cursor.fetchall()
    for req in armorRequirements:
        armorId = req[1]
        advancementId = req[0]
        # Check if the armor is already in armorReqs
        if armorId in armorReqs:
            armorReqs[armorId].append(advancementId)
        else:
            armorReqs[armorId] = [advancementId]

    query = "SELECT * FROM UnlocksWeapon"
    cursor.execute(query)
    weaponRequirements = cursor.fetchall()
    for req in weaponRequirements:
        weaponId = req[1]
        advancementId = req[0]
        # Check if the weapon is already in weaponReqs
        if weaponId in weaponReqs:
            weaponReqs[weaponId].append(advancementId)
        else:
            weaponReqs[weaponId] = [advancementId]


    # Get the item ID's we cannot get with current advancements, save in accessoryIds, armorIds, and weaponIds
    accessoryIds = []
    armorIds = []
    weaponIds = []
    for acc in accessoryReqs:
        for req in accessoryReqs[acc]:
            if req not in advancements:
                accessoryIds.append(acc)
                break
    for arm in armorReqs:
        for req in armorReqs[arm]:
            if req not in advancements:
                armorIds.append(arm)
                break
    for wep in weaponReqs:
        for req in weaponReqs[wep]:
            if req not in advancements:
                weaponIds.append(wep)
                break

    # Lookup items in DB
    query = "SELECT * FROM Accessory"
    if len(accessoryIds) > 0:
        i = True
        for accId in accessoryIds:
            if i:
                query += " WHERE AccessoryId != " + str(accId)
                i = False
            else:
                query += " AND AccessoryId != " + str(accId)
    cursor.execute(query)
    accessories = cursor.fetchall()

    query = "SELECT * FROM Armor"
    if len(armorIds) > 0:
        i = True
        for armId in armorIds:
            if i:
                query += " WHERE ArmorId != " + str(armId)
                i = False
            else:
                query += " AND ArmorId != " + str(armId)
    cursor.execute(query)
    armor = cursor.fetchall()

    query = "SELECT * FROM Weapon"
    if len(weaponIds) > 0:
        i = True
        for wepId in weaponIds:
            if i:
                query += " WHERE WeaponId != " + str(wepId)
                i = False
            else:
                query += " AND WeaponId != " + str(wepId)
    cursor.execute(query)
    weapons = cursor.fetchall()


    # Close the connection and return the items
    conn.close()
    response = {
        "accessories": accessories,
        "armor": armor,
        "weapons": weapons
    }
    return response

def get_advancements():
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database
    query = "SELECT * FROM Advancement"
    cursor.execute(query)
    advancements = cursor.fetchall()
    return advancements

def post_equipment(characterId, itemType, itemId):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Ensure the item exists
    if itemType == "weapon":
        query = "SELECT WeaponId FROM Weapon WHERE WeaponId = %s"
    elif itemType == "armor":
        query = "SELECT ArmorId FROM Armor WHERE ArmorId = %s"
    elif itemType == "accessory":
        query = "SELECT AccessoryId FROM Accessory WHERE AccessoryId = %s"
    cursor.execute(query, (itemId, ))
    if cursor.fetchone() is None:
        return False
    
    # Ensure armor slots are free
    if itemType == "armor":
        # Get the slot of the queried armor
        query = "SELECT ArmorSlot FROM Armor WHERE ArmorId = %s"
        cursor.execute(query, (itemId, ))
        armorSlot = cursor.fetchone()[0]
        # Check if the slot is already taken
        query = "SELECT ArmorId FROM Wears WHERE CharId = %s"
        cursor.execute(query, (characterId, ))
        equippedArmor = cursor.fetchall()
        for armor in equippedArmor:
            query = "SELECT ArmorSlot FROM Armor WHERE ArmorId = %s"
            cursor.execute(query, (armor[0], ))
            if cursor.fetchone()[0] == armorSlot:
                query = "DELETE FROM Wears WHERE CharId = %s AND ArmorId = %s"
                cursor.execute(query, (characterId, armor[0]))
                conn.commit()

    # Ensure an accessory slot is free
    if itemType == "accessory":
        # Get number of equiped accessories
        query = "SELECT COUNT(*) FROM Equips WHERE CharId = %s"
        cursor.execute(query, (characterId, ))
        accessoryCount = cursor.fetchone()[0]
        if accessoryCount >= 6:
            return False

    # Set the item
    if itemType == "weapon":
        query = "UPDATE TerrariaCharacter SET WeaponId = %s WHERE CharId = %s"
    elif itemType == "armor":
        query = "INSERT INTO Wears (ArmorId, CharId) VALUES (%s, %s)"
    elif itemType == "accessory":
        query = "INSERT INTO Equips (AccessoryId, CharId) VALUES (%s, %s)"
    cursor.execute(query, (itemId, characterId))
    conn.commit()

    # Close the connection and return 1 if successful
    conn.close()
    return True

if __name__ == "__main__":
    print(post_equipment(2,"armor",4))