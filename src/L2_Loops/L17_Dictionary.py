# like a two dimentional list
'''
students = ["Hermione", "Harry", "Malfoy"]
houses = ["griffin","griffin","slythrin"]

'''

students = {
    "Ron": "Griffindor",
    "Harry": "Griffindor",
    "Draco": "Slytherin"
}
'''
print(students["Draco"])
print(students["Harry"])
print(students["Ron"])

'''
for stud in students:
    print(stud, students[stud], sep=", ")
