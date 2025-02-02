import csv

students = []

with open("students2.csv") as file:
    # it will auto find all the commas, quotes and other corner cases
    reader = csv.reader(file)

    # for name, home in reader:
    #     students.append({"name": name, "home": home})          OR
    for row in reader:
        students.append({"name": row[0], "home": row[1]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
