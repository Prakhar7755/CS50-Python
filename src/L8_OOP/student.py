# TUPLE IMPLEMENTATION
'''
def main():
    student = get_student()
    if student[0] == "padma":
        student[1] = "Ravenclaw"
        # 'tuple' object does not support item assignment and will change in dictionary
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("name: ")
    house = input("house: ")
    #return (name, house)   # used a tuple(immutable) 
                           # return a tuple containing 2 things
    return [name, house] # list is mutable
'''

# DICTIONARY IMPLEMENTATION (mutable)


def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"

    print(f"{student['name']} from {student['house']}")


def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("house: ")
    # return student
    name = input("name: ")
    house = input("house: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
