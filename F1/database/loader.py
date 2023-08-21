from cs50 import SQL
import sys
import csv

db = SQL("sqlite:///f1.db")

if len(sys.argv) < 2:
    quit()

table_name, extension = sys.argv[1].split(".")

db.execute(
    "CREATE TABLE ? ("
    "driverID INTEGER NOT NULL,"
    "driverRef TEXT NOT NULL,"
    "number INTEGER,"
    "code TEXT NOT NULL,"
    "forename TEXT NOT NULL,"
    "surname TEXT NOT NULL,"
    "dob TEXT NOT NULL,"
    "nationality TEXT NOT NULL,"
    "url TEXT NOT NULL"
    ")", table_name
)


with open(sys.argv[1], "r") as file:
    reader = csv.reader(file)
    for line in reader:
        if line[0] != "driverId":
            driverId,driverRef,number,code,forename,surname,dob,nationality,url = line

            db.execute("INSERT INTO drivers (driverId,driverRef,number,code,forename,surname,dob,nationality,url) VALUES (?,?,?,?,?,?,?,?,?)", driverId,driverRef,number,code,forename,surname,dob,nationality,url

)
