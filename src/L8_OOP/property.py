# GETTERS AND SETTERS
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):                  # Getter (gets some attribute)
        return self._house  # _house

    @house.setter
    def house(self, house):           # Setter (sets some value)
        if house not in ["Griffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house  # _house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


def main():
    student = get_student()
    # raise the error in setter as i am assinging the wrong value
    # student.house = "Pivot Drive"
    student._house = "PICO DRIVE"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
