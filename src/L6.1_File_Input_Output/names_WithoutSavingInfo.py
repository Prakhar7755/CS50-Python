# Information provided to a program erased when the program ends

# File I/O is all about writing code that can read from(load info. from) or
# write to(save info. to) files themselves


# list

names = []

for _ in range(3):
    # name = input("What's your name? ")
    # names.append(name) # adding name to the list of names

    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")


    







