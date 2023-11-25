chars = [x for x in input() if x != " "]
letters = {}
for char in chars:
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")