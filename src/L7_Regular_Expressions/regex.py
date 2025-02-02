import re

email = input("Whats your email? ").strip().lower()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu|gov|net|org|in)$", email, re.IGNORECASE):  # multiple dots
    print("Valid")  # (\w+\.)? for multiple dots or use [a-zA-z0-9_.]
else:
    print("Invalid")
