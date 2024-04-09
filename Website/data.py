import mysql.connector
from dotenv import load_dotenv
import os, hashlib, re


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
def post_login(username: str, password: str) -> str | None:
    """
    Logs in a user. Returns random Session token or `None` if no user is found.
    """
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
def delete_login(token: str) -> bool:
    """Logs out a user. Returns `true` if successful, `false` otherwise."""
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
def get_loggedin_user(token: str) -> dict:

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


def update_password(userId: int, password: str):
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


def get_characters(userId: int):
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

def delete_character(charId: int):
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

def get_items(advancements: list[int]) -> list[int]:
    """ 
    Takes a list of advancement ID's and produces a corresponding list of Item IDs.
    i.e. Queries the database to find what items can be accessed for given advancements.

    Meant to be used as part of the 'filter' for the Home page.
    """
    accessoryReqs = {}
    armorReqs = {}
    weaponReqs = {}

    if advancements == "None":
        advancements = []

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

def get_advancements() -> list[(int, str)]:
    """
    Returns a `list` of tuples containing (advancementId, advancementName)
    """
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database
    query = "SELECT * FROM Advancement"
    cursor.execute(query)
    advancements = cursor.fetchall()
    return advancements

def post_equipment(characterId: int, itemType: str, itemId: int) -> bool:
    """
    Attempts to equip an item of `itemId` and `itemType` to a given character whose id is `characterId`.
    
    Returns `False` if there are issues (such as the item not existing, or the slot already being occupied), `True` otherwise.
    """
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
        
        # Check if the accessory is already equiped
        query = "SELECT AccessoryId FROM Equips WHERE CharId = %s AND AccessoryId = %s"
        cursor.execute(query, (characterId, itemId))
        if cursor.fetchone() is not None:
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

def get_character(charId):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database
    query = "SELECT CharName, WeaponId FROM TerrariaCharacter WHERE CharId = %s"
    cursor.execute(query, (charId, ))
    character = cursor.fetchone()

    # Close the connection and return the character
    conn.close()
    return {
        "Name": character[0],
        "weaponId": character[1]
    }

def get_armor(armorId):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database
    query = "SELECT ArmorName, ImageURL, StatDefense, StatBonus, ArmorSlot, ArmorID FROM Armor WHERE ArmorId = %s"
    cursor.execute(query, (armorId, ))
    armor = cursor.fetchone()



    # Close the connection and return the armor
    conn.close()
    return {
        "ArmorName": armor[0],
        "ImageURL": re.sub('/revision.*', '', armor[1]),
        "StatDefense": armor[2],
        "StatBonus": armor[3],
        "ArmorSlot": armor[4],
        "ArmorID": armor[5]
    }

def get_character_armor(charId):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database
    query = "SELECT ArmorId FROM Wears WHERE CharId = %s"
    cursor.execute(query, (charId, ))
    armor = cursor.fetchall()

    # Close the connection and return the armor
    conn.close()
    return armor

def get_equips(charId):
    # Connect to database and establish cursor
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database
    query = "SELECT AccessoryId FROM Equips WHERE CharId = %s"
    cursor.execute(query, (charId, ))
    accessories = cursor.fetchall()

    # Close the connection and return the accessories
    conn.close()
    return accessories

def get_accessories(accessoryID):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT AccessoryName, ImageURL, StatBonus, AccessoryID FROM Accessory WHERE AccessoryId = %s"
    cursor.execute(query, (accessoryID, ))
    accessory = cursor.fetchone()

    conn.close()

    return {
        "AccessoryName": accessory[0],
        "ImageURL": re.sub('/revision.*', '', accessory[1]),
        "StatBonus": accessory[2],
        "AccessoryID": accessory[3]
    }