students = []  # empty list

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # student = {}  # empty dictionary
        # student["name"] = name
        # student["house"] = house
        # students.append(student)  OR
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):    # for sortin the name
    return student["name"]


def get_house(student):   # for sortin the house
    return student["house"]


# passing a func() to another func()

# sorting by name
'''
for student in sorted(students, key=get_name, reverse=True):
     print(f"{student['name']} is in {student['house']}")
'''

# sorting by house
for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}")
