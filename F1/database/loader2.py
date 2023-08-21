import csv
from cs50 import SQL

db = SQL("sqlite:///f1.db")

db.execute(
    "CREATE TABLE seasons ("
    "year INTEGER NOT NULL,"
    "url TEXT NOT NULL"
    ")"
)

with open("seasons.csv", "r") as file:
    reader = csv.reader(file)

    for line in reader:
        if line[0] != "year":
            year, url = line
            db.execute("INSERT INTO seasons (year, url) VALUES (?,?)", year, url)
