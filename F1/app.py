from flask import Flask, flash, redirect, render_template, request, session
import requests
from cs50 import SQL
from helpers import calculate_relevance_score, get_country, get_flag, get_image, get_layout, get_logo, capitalize

app = Flask(__name__)

db = SQL("sqlite:///f1.db")
log = SQL("sqlite:///log.db")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/drivers", methods=["GET", "POST"])
def drivers():
    if request.method == "POST":
        option = int(request.form.get("showing"))
        if not request.form.get("showing") or option == 0:
            drivers = db.execute("SELECT * FROM drivers")
            return render_template("drivers.html", drivers=drivers, option=option)

        drivers = db.execute("SELECT * FROM drivers LIMIT ?", option)
        return render_template("drivers.html", drivers=drivers, option=option)

    drivers = db.execute("SELECT * FROM drivers")
    option = 50

    return render_template("drivers.html", drivers=drivers, option=option)

@app.route("/constructors", methods=["GET", "POST"])
def constructors():
    constructors = db.execute("SELECT * FROM constructors")

    return render_template("constructors.html", constructors=constructors)

@app.route("/circuits", methods=["GET", "POST"])
def circuits():
    circuits = db.execute("SELECT * FROM circuits")

    return render_template("circuits.html", circuits=circuits, get_layout=get_layout)

@app.route("/seasons", methods=["GET", "POST"])
def seasons():
    seasons = db.execute("SELECT * FROM seasons")

    return render_template("seasons.html", seasons=seasons, get_logo=get_logo)

@app.route("/hall-of-fame/drivers", methods=["GET", "POST"])
def hof_drivers():
    drivers = db.execute("SELECT * FROM drivers_hof")
    return render_template("hof-drivers.html", drivers=drivers)

@app.route("/hall-of-fame/constructors", methods=["GET", "POST"])
def hof_constructors():
    constructors = db.execute("SELECT * FROM constructors_hof")
    return render_template("hof-constructors.html", constructors=constructors)

@app.route("/quizzes", methods=["GET", "POST"])
def quizzes():
    return render_template("quizzes.html")

@app.route("/quizzes/drivers-championship", methods=["GET", "POST"])
def drivers_quiz():
    drivers = db.execute("SELECT forename, surname FROM drivers ORDER BY forename, surname")
    drivers = [driver["forename"] + " " + driver["surname"] for driver in drivers]
    answers = db.execute("SELECT year, driver FROM seasons ORDER BY year DESC")
    years = list(range(2022, 1949, -1))

    if request.method == "POST":
        user_inputs = {}
        for year in years:
            user_inputs[year] = request.form.get(str(year))
        right_answers = {}
        for year in years:
            user_guess = request.form.get(str(year))
            answer_index = next((index for index, entry in enumerate(answers) if entry['year'] == year), None)

            if user_guess and answer_index is not None:
                if user_guess.lower() == answers[answer_index]['driver'].lower():
                    right_answers[year] = answers[answer_index]['driver']

        return render_template("quiz-result.html", years=years, answers=answers, right_answers=right_answers, right_answers_amount=len(right_answers), test=request.form.get("2022"), inputs=user_inputs, capitalize=capitalize)
    right_answers = {}
    return render_template("drivers-championship.html", years=years, drivers=drivers,)

@app.route("/quizzes/constructors-championship", methods=["GET", "POST"])
def constructors_quiz():
    answers = db.execute("SELECT year, team FROM seasons ORDER BY year DESC")
    years = list(range(2022, 1957, -1))

    return render_template("constructors-championship", years)

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        if not request.form.get("search"):
            return redirect("/")

        search_input = request.form.get("search")
        drivers = db.execute("SELECT driverRef, forename, surname, nationality, url FROM drivers")
        driver_query = [
            (driver, calculate_relevance_score(search_input, driver["forename"], driver["surname"])) for driver in drivers
        ]
        driver_query.sort(key=lambda x: x[1], reverse=True)

        constructors = db.execute("SELECT constructorRef, name, nationality, url FROM constructors")
        constructors_query = [
            (constructor, calculate_relevance_score(search_input, constructor["name"])) for constructor in constructors
        ]
        constructors_query.sort(key=lambda x: x[1], reverse=True)

        circuits = db.execute("SELECT circuitRef, name, country, url FROM circuits")
        circuits_query = [
            (circuit, calculate_relevance_score(search_input, circuit["circuitRef"])) for circuit in circuits
        ]
        circuits_query.sort(key=lambda x: x[1], reverse=True)

        return render_template("search.html", search=search_input, driver_query=driver_query[:25], constructors_query=constructors_query[:15], circuits_query=circuits_query[:5],get_country=get_country, get_flag=get_flag)

    return redirect("/")

@app.route("/report", methods=["GET", "POST"])
def report():
    invalid_fields = []
    if request.method == "POST":
        correction = request.form.get("report-input")
        page = request.form.get("page")
        field = request.form.get("field")
        Id = request.form.get("id")
        feedback = request.form.get("feedback")

        if correction.strip() == "":
            invalid_fields.append("correction")

        selections = {"page": page, "field": field}

        for selection in selections:
            if selections[selection] == None:
                if "page" not in invalid_fields:
                    invalid_fields.append(selection)

        id_limits = {"Drivers": 857, "Constuctors": 211, "Circuits": 77, "Seasons": 2022}

        if request.form.get("id") == None or request.form.get("id") == 0:
            invalid_fields.append("id")
            invalid_fields.append(request.form.get("id"))

        if request.form.get("id") != None:
            for page in id_limits:
                if int(request.form.get("id")) > id_limits[page]:
                    invalid_fields.append("id")
                elif page == "Seasons":
                    if int(request.form.get("id")) < 1950:
                        invalid_fields.append("id")

        if len(invalid_fields) != 0:
            return render_template("reported.html", invalid_fields=invalid_fields)

        time = db.execute("SELECT strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime') AS current_time")[0]["current_time"]
        log.execute("INSERT INTO error_reports (correction, page, field, id, feedback, time) VALUES (?,?,?,?,?,?)", correction, page, field, Id, feedback, time)
        return render_template("reported.html")

    return render_template("report.html", invalid_fields=invalid_fields)

@app.route("/credits", methods=["GET"])
def credits():
    return render_template("credits.html")