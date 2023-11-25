phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, number = entry.split("-")
    if name not in phonebook.keys():
        phonebook[name] = 0
    phonebook[name] = number

for i in range(int(entry)):
    name = input()
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")