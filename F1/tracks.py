import csv
from helpers import get_image_hd

tracks = {}

with open("database/tracks.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        track, url = line
        tracks[track] = get_image_hd(track)


with open("database/tracks2.csv", "a") as file:
    for track in tracks:
        file.write(f"{track},{tracks[track]}\n")



print(tracks)