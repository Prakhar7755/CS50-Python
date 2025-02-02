name = input("What's your name? ")

# with (this context) i want to open and automatically close some file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")





