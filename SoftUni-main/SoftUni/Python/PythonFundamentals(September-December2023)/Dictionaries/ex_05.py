items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
while not obtained:
    current_items = input().split()
    for i in range(0, len(current_items), 2):
        value = int(current_items[i])
        key = current_items[i+1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break

for key, value in items.items():
    print(f"{key}: {value}")