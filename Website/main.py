import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from data import post_login

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        token = post_login(username, password)
        if token is None:
            flash("Invalid username or password")
            return redirect(url_for("login"))
        # return redirect()
        return "Logged in"
    
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)