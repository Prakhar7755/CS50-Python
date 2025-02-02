
import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students3.csv", "a") as file:
    # writer = csv.writer(file)  # write
    # writer.writerow([name,home])

    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    # i can interchange this as well because it wont affect (down)
    writer.writerow({"name": name, "home": home})
