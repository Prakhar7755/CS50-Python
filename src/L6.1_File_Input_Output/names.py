name = input("What's your name? ")

# open function (double clicking)

file = open("names.txt", "a")
# name of the file where all of this will be saved
# "w" means write to this file OR  tell open to open a file that allow me
# "a" means to append/add to the file (no gaps in between earliar)
# to change its content or create that file


# file.write(name)
file.write(f"{name}\n") # makes the entries in next line instead of same



# file.close  # closing and saving 
