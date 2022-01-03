import sqlite3
from flask import Flask, redirect, render_template, request


app = Flask(__name__)


def get_registrants(path: str = "database/flaskapp.db"):
    with sqlite3.connect(path) as con:
        cur = con.cursor()
        data = cur.execute("SELECT * from registrants")
    return data


def insert_registrant(name: str, sport: str, path: str = "database/flaskapp.db"):
    with sqlite3.connect(path) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport))


SPORTS = [
    "Dodgeball",
    "Handball",
    "Basketball",
    "Soccer",
    "Volleyball"
]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name:
        result = render_template("error.html", message="Missing name")
    elif not sport:
        result = render_template("error.html", message="Missing sport")
    elif sport not in SPORTS:
        result = render_template("error.html", message="Invalid sport")
    else:
        insert_registrant(name, sport)
        result = redirect("/registrants")
    return result


@app.route("/registrants")
def registrants():
    registrants = get_registrants()
    return render_template("registrants.html", registrants=registrants)