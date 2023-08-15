'''
name = input("What your name is ")


# REMOVE WHITESAPACE FROM THE STR
name = name.strip()  #    REMOVE ALL SHITTY SPACES
print(f"hello, {name}") 


name = name.capitalize() # capitalize the first letter 
print(f"hello, {name}") 


name = name.title()  # capitalize every letter
print(f"hello, {name}") 


name = name.strip().title()   
'''

                                # BEST WAY TO WRITE ALL THESE THING

name = input("what's your name ? ").strip().title()   

print(f"hello, {name}")

# splitting the name is first name and last name 

# name.split 
first, last = name.split(" ")  # takes 2 input only

print(f"hello, {first}")   # return the first name  [hello, David]









