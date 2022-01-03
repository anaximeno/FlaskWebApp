import sqlite3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

REGISTRANTS = {

}


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
        REGISTRANTS[name] = sport
        print(REGISTRANTS)
        result = redirect("/registrants")
    return result


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)