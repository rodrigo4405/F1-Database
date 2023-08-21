import csv
from cs50 import SQL

db = SQL("sqlite:///f1.db")



with open("database/teams_entries.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        team,first,last = line
        db.execute("UPDATE constructors SET first = ?, last = ? WHERE name = ?", first,last,team)
