import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from data import post_login, get_loggedin_user, update_password, delete_login, get_characters, add_character, delete_character, get_advancements, get_character, get_armor, get_character_armor, get_equips, get_accessories


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

    itemCardList = [] # List of Strings
    # For each item in `filtered_items`
        # Render an HTML 'card' for that item using the template
        # Store the card in `itemCardList`

    # For each itemCard in `itemCardList`
        # Add it as an entry in the table
    
    # Insert table into index.html template
    return render_template("index.html", advancements=advancements, selectedAdv=selectedAdv)

    if request.method == "POST":
        # (i.e. if the user has just submitted a new set of filters)
        # Get the latest filters from the cookie
        
        # Acquire the list of items as a result of the filters
        print()


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

      

    return render_template("account.html", user=user, characters=get_characters(user["userId"]), selcharacter=str(selcharacter))

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


@app.route("/character")
def characters():
    # Check if the user is logged in
    if request.cookies.get("token") is None:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for("login"))
    
    armor = []
    accessories= []
    # Get the user from the database
    user = get_loggedin_user(request.cookies.get("token"))
    charID = request.cookies.get("character")
    char = get_character(charID)
    armorID = get_character_armor(charID)
    for i in armorID:
        armor.append(get_armor(i[0]))

    accessoryID = get_equips(charID)
    for i in accessoryID:
        accessories.append(get_accessories(i[0]))
    
    return render_template("character.html", user=user, char=char, armor=armor, accessories=accessories)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)