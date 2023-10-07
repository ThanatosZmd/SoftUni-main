ints = list(map(int, input().split(", ")))
count_beggars = int(input())
beggars = []
index = 0
while True:
    if index >= len(ints) and len(beggars) == count_beggars:
            break
    for i in range(count_beggars):
        if index >= len(ints) and len(beggars) == count_beggars:
            break
        if len(beggars) == count_beggars and len(ints) > index:
            beggars[i] += ints[index]
        else:
            if index>=len(ints):
                beggars.append(0)
            else:
                beggars.append(ints[index])
        index += 1

print(beggars)