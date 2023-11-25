import re

data = input().split(", ")
pattern = r"[a-zA-Z0-9\-\_]+"
for user in data:
    matches = re.findall(pattern, user)
    if matches[0] == user and 3<=len(user)<=16 and " " not in user:
        print(user)