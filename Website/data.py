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