import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from data import post_login, get_loggedin_user, update_password, delete_login


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
    print(request.cookies.get("token"))
    return render_template("index.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    # Check if the user is logged in
    if request.cookies.get("token") is None:
        return redirect(url_for("login"))
    # Get the user from the database
    user = get_loggedin_user(request.cookies.get("token"))
    
    if request.method == "POST":
        # Get the password and confirm password from the form
        password = request.form["inputPassword"]
        comfirm_password = request.form["inputPasswordconfirm"]

        # Check if the passwords match
        if password != comfirm_password:
            # If they don't match, flash a message and return the user to the account page
            flash("Passwords do not match")
        
        # Update the password in the database
        update_password(user["userId"], password)

    return render_template("account.html", user=user)

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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")