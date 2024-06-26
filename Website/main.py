import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from dotenv import load_dotenv
from data import *
import re
import init

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
    
    #if get_loggedin_user(request.cookies.get("token")) is None:
    #    return redirect(url_for("login"))
    
    selectedAdv = str(request.cookies.get("filters"))
    
    # Generate dummy data for all advancements
    advancements = get_advancements()

    # Get the user from the database
    #user = get_loggedin_user(request.cookies.get("token"))

    # Acquire the list of items as a result of the filters
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
            "description": "Type: " + weaponsRaw[i][4] + " | Damage: " + weaponsRaw[i][3] + " | Knockback: " + weaponsRaw[i][5] + " | Crit: " + weaponsRaw[i][6] + " | Time: " + weaponsRaw[i][7],
            "type": "Weapon"
        }
        weapons.append(weapon)

    for i in range(len(armorRaw)):
        fixedImage = re.sub('/revision.*', '', armorRaw[i][2])
        armorPiece = {
            "id": armorRaw[i][0],
            "name": armorRaw[i][1],
            "image": fixedImage,
            "description": "Defense: " + str(armorRaw[i][3]) + " | " + armorRaw[i][4],
            "type": "Armor"
        }
        armor.append(armorPiece)

    # Check if the user has selected a character
    equippedWeapon = ""
    equippedArmor = []
    equippedAccessories = []
    charId = request.cookies.get("character")
    if charId is not None and charId is not "":
        charId = int(charId)
        equippedWeapon = get_character_weapon(charId)
        equippedArmorRaw = get_character_armor(charId)
        for i in equippedArmorRaw:
            equippedArmor.append(i[0])
        equippedAccessoriesRaw = get_equips(charId)
        for i in equippedAccessoriesRaw:
            equippedAccessories.append(i[0])

    
    # Insert table into index.html template
    return render_template("index.html", advancements=advancements, selectedAdv=selectedAdv, accessories=accessories, weapons=weapons, armor=armor, numCols=4, equippedWeapon=equippedWeapon, equippedArmor=equippedArmor, equippedAccessories=equippedAccessories)

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
    if type(result) == str:
        return jsonify({"error": result, "success": False})
    return jsonify({"success": True})



@app.route("/account", methods=["GET", "POST"])
def account():
    # Check if the user is logged in
    if request.cookies.get("token") is None:
        return redirect(url_for("login"))
    
    #if get_loggedin_user(request.cookies.get("token")) is None:
    #    return redirect(url_for("login"))
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
    return render_template("clearTokens.html")


@app.route("/character", methods=["GET", "POST"])
def characters():
    # Check if the user is logged in
    if request.cookies.get("token") is None:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for("login"))
    
    #if get_loggedin_user(request.cookies.get("token")) is None:
    #    return redirect(url_for("login"))
    
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

    defence = 0
    for a in armor:
        defence += a["StatDefense"]
    
    return render_template("character.html", user=user, char=char, armor=armor, accessories=accessories, weapon=weapon, defence=defence)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if password != confirm_password:
            flash("Passwords do not match")
            return redirect(url_for("register"))
        
        result = post_register(username, password)
        if type(result) == str:
            flash(result)
            return redirect(url_for("register"))
        return redirect(url_for("login"))
    
    return render_template("register.html")




if __name__ == "__main__":
    init.init()
    app.run(debug=True, host="0.0.0.0", port=8001)