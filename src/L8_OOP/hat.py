import random


class Hat:

    houses = ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod  # help me that we now don't need any object on 14
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))  # cls means class


# hat = Hat()
# hat.sort("Harry")
Hat.sort("Harry")


2:11:00