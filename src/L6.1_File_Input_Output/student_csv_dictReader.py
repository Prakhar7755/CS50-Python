# csv.DictReader
import csv

students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file)  # USING A DICTIONARY READER

    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
