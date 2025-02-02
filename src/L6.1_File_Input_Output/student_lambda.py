# using lambda function
students = []

with open("students2.csv") as file: # it will break because of multiple commas in student2 not in student.csv
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)

# this syntax is equivalent to the previous sorting syntax using func()
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")


