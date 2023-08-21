import csv
from cs50 import SQL

db = SQL("sqlite:///f1.db")

with open("database/circuit_length.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        name,length,type = line
        db.execute("UPDATE circuits SET name = ? WHERE length = ?", name, length)