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
    if request.cookies.get("token") is None:
        return redirect(url_for("login"))
    user = get_loggedin_user(request.cookies.get("token"))
    
    if request.method == "POST":
        password = request.form["inputPassword"]
        comfirm_password = request.form["inputPasswordconfirm"]
        if password != comfirm_password:
            flash("Passwords do not match")
        
        update_password(user["userId"], password)

    return render_template("account.html", user=user)

@app.route("/logout")
def logout():
    if request.cookies.get("token") is None:
        return redirect(url_for("login"))
    
    delete_login(request.cookies.get("token"))
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)