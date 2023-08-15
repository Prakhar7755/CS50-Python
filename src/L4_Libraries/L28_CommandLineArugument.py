import sys

# BASIC IMPLEMENTATION AND IT WILL GIVE ERROR IF NOT GIVEN 2 ARGS
"""
# Get the username and password from command line args
username = sys.argv[1]
password = sys.argv[2]

# Print them out
print(f"Username is {username}")
print(f"Password is {password}")
"""
# CHECKING IF THE NUMBER OF ARGS ENTERED IS ENOUGH OR NOT
'''
try:
    print("Hello, My Name Is", sys.argv[1])

except IndexError:
    print("Too few arguments or you can give one arg only") 

'''

# A BETTER WAY TO CHECK IF THE NUMBER OF ARGUMENT ARE ENOUGH OR NOT
'''
if len(sys.argv) < 2 :
    print("too few arguments")

elif len(sys.argv) > 2 :
    print('too many arguments')

else:
    print("Hello, My Name Is", sys.argv[1])
'''
# CAN USE double quotes "David J. Malan" for 3 words in a single argument

# using SYS.EXIT() FUNCTION without else
'''
if len(sys.argv) < 2 :
    sys.exit("too few arguments")
elif len(sys.argv) > 2 :
    sys.exit('too many arguments')


print("Hello, My Name Is", sys.argv[1])
'''

# USING LOOPS FOR MULTIPLE ARGUMENTS

if len(sys.argv) < 2 :
    sys.exit("too few arguments")

for arg in sys.argv[1:] :                 # slice [1:(no end)] tells that start with 1st index
    print("hello, my name is", arg)
