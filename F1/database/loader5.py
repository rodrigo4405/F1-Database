import csv
from cs50 import SQL

db = SQL("sqlite:///f1.db")

with open("database/champions.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        year,driver,team = line
        db.execute("UPDATE seasons SET driver = ?, constructor = ? WHERE year = ?",driver,team,year)