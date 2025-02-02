# reformat the users input in the format we expect

import re

name = input("What's your name? ").strip()
'''
# return boolean AND used brackets to capture the things
matches = re.search(r"^(.+), *(.+)$", name) # ? or * ask space is not mandatory

if matches:  # WILL ONLY BE EXECUTED IF IT MATCHES THE ABOVE FORMAT else it will print
    # last, first = matches.groups()
    # name = f"{first} {last}"
    last = matches.group(1)  # start with 1 not 0
    first = matches.group(2)
    name = f"{first} {last}"  # or use matches.group(2) +" "+ matches.group(1)

print(f"hello, {name}")

'''

if matches := re.search(r"^(.+), *(.+)$", name) # := walrus operator 

    name = use matches.group(2) +" "+ matches.group(1)

print(f"hello, {name}"










# (...) a group
# (?:...) non capturing version


'''
if "," in name:
    last, first = name.split(", ") 
    name = f"{first} {last}"

print(f"hello, {name}")
'''
