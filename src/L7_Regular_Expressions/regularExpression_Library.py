import re
email = input("Whats your email? ").strip().lower()

# if re.search("@", email): # re.search(pattern , string , flags=0)
# if re.search(".+{1}@.+", email):
# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):  # anything except @ in []
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):  # set of allowed characters

if re.search(r"^\w+@\w+\.(com|edu|gov|net|org|in)$", email, re.IGNORECASE):  # this will work as well
    print("Valid")
else:
    print("Invalid")


"""Regular expressions"""
# . any character except newline
# * 0 or more repetition
#    ..* => .+  both may work
# + 1 or more
# ? 0 or 1 reptition
# {m} m repetition
# {m,n} m-n repetition
# ^ matches the start of the string  {Exact match nothing extra}
# $ matches the end of the string or just before the newline at the end of the string
# [] set of character
# [^] complementing the set {cannot match anything like this}
'''
\d decimal digit
\D not a decimal digit
\s whitespace char
\S not a whitespace
\w word char + number + underscore(_)
\W not a word character

A|B either A or B
(...) a group
(?:...) non-capturing version
'''
