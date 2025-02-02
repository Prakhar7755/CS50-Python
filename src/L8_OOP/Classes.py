class Student:
    # to initialize the contents of an obj from a class
    # self is a default argument
    def __init__(self, name, house):

        if not name:
            raise ValueError("Missing Name")

        if house not in ["Griffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            raise ValueError("Invalid House")

        self.name = name  # self gives access to current obj that was created
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"



def main():
    student = get_student()
    # student.house = "DON'T KNOW" # mutable
    # print(f"{student.name} from {student.house}")
    print(student)


'''
def get_student():
    student = Student()       creating an object/instance/incarnation of Student Class
    student.name = input("Name: ").strip()
    student.house = input("House: ").strip()
    return student
'''


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  # constructor


if __name__ == "__main__":
    main()
    # def charm(self):           WE CREATED THIS METHOD
    #     match.self.patronus:
    #         case "Stag":
    #           return ""
