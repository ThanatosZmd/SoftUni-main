data = input().split(" ")
for el in data:
    new_el = int(el)
    if new_el < 0:
        new_el = abs(new_el)
    else:
        new_el = -abs(new_el)
    data[data.index(el)] = new_el
print(data)