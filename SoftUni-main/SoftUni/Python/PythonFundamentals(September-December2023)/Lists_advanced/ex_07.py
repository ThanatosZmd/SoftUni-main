data = list(map(int, input().split(", ")))
groups = []
lower_limit = 0
upper_limit = 10
while data:
    group = []
    for i in range(len(data)):
        if data[i] >= lower_limit and data[i] <= upper_limit:
            group.append(data[i])
    for x in range(len(group)):
        if group[x] in data:
            data.remove(group[x])
    groups.append(group)
    lower_limit = upper_limit
    upper_limit += 10

for i in range(1, len(groups)+1):
    print(f"Group of {i}0's: {groups[i-1]}")