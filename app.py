from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3


app = Flask(__name__)

# config sesion
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

cur = sqlite3.connect("users.db")
db = cur.cursor()

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST  "])
def login():
    if request.method == "GET":
        return render_template("logint.html")
    ...