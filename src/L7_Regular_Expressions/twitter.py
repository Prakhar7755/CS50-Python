'''
url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
username = url.removeprefix("https://twitter.com/")

print(f"Username: {username}")
'''

import re
'''
url = input("URL: ").strip()
# re.sub(pattern, repl, string, count=0, flags=0)
# remeber the dot in the website
# ? mark for http or https
# https may not be present 

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)  # best

print(f"Username: {username}")
'''
url = input("URL: ").strip()
if matches := re.search(r"https?://(?:www\.)?twitter\.(?:com|org)/([a-zA-Z0-9_]+)", url, re.IGNORECASE):
    # (.+)  and not capturing www by using (?:...)
    print(f"Username:", matches.group(1))


'''

re.split()
re.findall()

'''