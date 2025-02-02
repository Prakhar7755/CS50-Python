# "r" means read/load a repo
'''
with open("names.txt", "r") as file:    # "r" means read/load a repo
    lines = file.readlines()  # reading all lines and storing them in this variable

for line in lines:
    print("hello,", line.rstrip())
    # print("hello,",line,end="") # gives an extra line  OR
'''

# Short way to do above thing
'''
with open("names.txt", "r") as file:
    for line in file:     # using a loop
        print("hello,", line.rstrip())
'''
# printing the names in sorted way
'''
names = []

with open("names.txt") as file:    # "r" with or without
    for line in file:
        names.append(line.rstrip())  # adding to the list names

for name in sorted(names):
    print(f"hello, {name}")
'''
# another shorter way to sort and print                     PREFER THIS FOR ME

'''
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

'''

# sorted(names, reverse = True) USE THIS FOR REVERSE SORTING

names = []

with open("names.txt") as file:    # "r" with or without
    for line in file:
        names.append(line.rstrip())  # adding to the list names

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
