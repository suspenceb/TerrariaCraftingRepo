import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from dotenv import load_dotenv
from data import *
import re

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET")

@app.route("/favicon.ico")
def favicon():
    return redirect(url_for("static", filename="favicon.ico"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        token = post_login(username, password)
        if token is None:
            flash("Invalid username or password")
            return redirect(url_for("login"))
        return render_template("saveToken.html", token=token)
    
    return render_template("login.html")

@app.route("/")
def index():
    # print(request.cookies.get("token"))
    if request.cookies.get("token") is None:
        return redirect(url_for("login"))
    
    selectedAdv = str(request.cookies.get("filters"))
    
    # Generate dummy data for all advancements
    advancements = get_advancements()

    # Get the user from the database
    user = get_loggedin_user(request.cookies.get("token"))

    # Acquire the list of items as a result of the filters
    # filtered_items = get_items(advancementLIst)

    filteredItems = get_items(selectedAdv)

    accessoriesRaw = filteredItems["accessories"]
    weaponsRaw = filteredItems["weapons"]
    armorRaw = filteredItems["armor"]

    accessories = []
    weapons = []
    armor = []

    # Convert the list of tuples to a list of dictionaries
    for i in range(len(accessoriesRaw)):
        fixedImage = re.sub('/revision.*', '', accessoriesRaw[i][2])
        accessory = {
            "id": accessoriesRaw[i][0],
            "name": accessoriesRaw[i][1],
            "image": fixedImage,
            "description": accessoriesRaw[i][3],
            "type": "Accessory"
        }
        accessories.append(accessory)

    for i in range(len(weaponsRaw)):
        fixedImage = re.sub('/revision.*', '', weaponsRaw[i][2])
        weapon = {
            "id": weaponsRaw[i][0],
            "name": weaponsRaw[i][1],
            "image": fixedImage,
            "description": weaponsRaw[i][3],
            "type": "Weapon"
        }
        weapons.append(weapon)

    for i in range(len(armorRaw)):
        fixedImage = re.sub('/revision.*', '', armorRaw[i][2])
        armorPiece = {
            "id": armorRaw[i][0],
            "name": armorRaw[i][1],
            "image": fixedImage,
            "description": armorRaw[i][3],
            "type": "Armor"
        }
        armor.append(armorPiece)
    
    # Insert table into index.html template
    return render_template("index.html", advancements=advancements, selectedAdv=selectedAdv, accessories=accessories, weapons=weapons, armor=armor)

@app.route("/equipItem", methods=["POST"])
def equipItem():
    data = request.json
    item_id = int(data.get('itemid'))
    item_type = data.get('itemtype')
    charId = int(request.cookies.get("character"))
    userId = get_loggedin_user(request.cookies.get("token"))["userId"]
    
    # Ensure that the character is owned by the user
    ownedCharacters = get_user_characters(userId)
    ownedCharacterIds = []
    for i in ownedCharacters:
        ownedCharacterIds.append(i["charId"])
    if charId not in ownedCharacterIds:
        print("error")
        return jsonify({"error": "Character not owned by user"})

    result = post_equipment(charId, item_type, item_id)
    print(result)



@app.route("/account", methods=["GET", "POST"])
def account():
    # Check if the user is logged in
    if request.cookies.get("token") is None:
        return redirect(url_for("login"))
    # Get the user from the database
    user = get_loggedin_user(request.cookies.get("token"))
    selcharacter = request.cookies.get("character")
    
    if request.method == "POST":
        try:
            # Get the password and confirm password from the form
            password = request.form["inputPassword"]
            comfirm_password = request.form["inputPasswordconfirm"]

            # Check if the passwords match
            if password != comfirm_password:
                # If they don't match, flash a message
                #  and return the user to the account page
                flash("Passwords do not match")
                
            # Update the password in the database
            update_password(user["userId"], password)
        except:
            pass
        try:
            newCharacter = request.form["charName"]
            print(newCharacter)

            # Add the new character to the database
            add_character(user["userId"], newCharacter)
        except:
            pass

        try:
            charId = request.form["delete"]
            delete_character(charId)

        except:
            pass

      

    return render_template("account.html", user=user, characters=get_user_characters(user["userId"]), selcharacter=str(selcharacter))

@app.route("/logout")
def logout():
    # Check if the user is logged in
    if request.cookies.get("token") is None:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for("login"))
    
    # Delete the login from the database
    delete_login(request.cookies.get("token"))
    
    # Redirect to the login page
    return redirect(url_for("login"))


@app.route("/character", methods=["GET", "POST"])
def characters():
    # Check if the user is logged in
    if request.cookies.get("token") is None:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for("login"))
    
    charID = request.cookies.get("character")
    if charID is None:
        flash("Please select a character")
        return redirect(url_for("account"))
    charID = str(charID)
    
    if request.method == "POST":
        try:
            armorID = request.form["remove_armor"]
            remove_armor(charID, armorID)
            
        except:
            pass

        try:
            accessoryID = request.form["remove_accessory"]
            remove_accessory(charID, accessoryID)
        except:
            pass

        try:
            weaponID = request.form["remove_weapon"]
            remove_weapon(charID)
        except:
            pass
    
    armor = []
    accessories= []
    # Get the user from the database
    user = get_loggedin_user(request.cookies.get("token"))
    char = get_character(charID)
    armorID = get_character_armor(charID)
    for i in armorID:
        armor.append(get_armor(i[0]))

    accessoryID = get_equips(charID)
    for i in accessoryID:
        accessories.append(get_accessories(i[0]))

    weaponID = str(get_character_weapon(charID))
    if weaponID != "None":
        weapon = get_weapon(str(weaponID))
    else:
        weapon = None


    
    return render_template("character.html", user=user, char=char, armor=armor, accessories=accessories, weapon=weapon)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)