# strip at the end to avoid whitespace at end
email = input("Whats your email? ").strip()

'''
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
'''

username, domain = email.split("@")

# if (username) and ("." in domain):
if (username) and domain.endswith("edu" or "com" or "in"):
    print("Valid")
else:
    print("Invalid")
