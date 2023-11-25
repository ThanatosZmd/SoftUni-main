data = input()
new_data = ""
power = 0
for i in range(len(data)):
    if data[i] != ">" and power>0:
        power -= 1
    elif data[i] == ">":
        new_data += data[i]
        power += int(data[i+1])
    else:
        new_data += data[i]
print(new_data)