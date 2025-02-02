'''
with open("students.csv") as file:
    for line in file:
        # row operation
        row = line.rstrip().split(",")  # striping and spliting at the same time

        print(f"{row[0]} is in {row[1]}")
'''
# another easy way

'''
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
'''

# Sorting this now
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
'''

# using another dictionary

students = []  # empty list

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        #student = {}  # empty dictionary
        # student["name"] = name
        # student["house"] = house
        # students.append(student)  OR
        student = {"name":name,"house":house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")



