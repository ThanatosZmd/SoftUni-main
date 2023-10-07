factor = int(input())
count = int(input())
l = []
begin = 1
while len(l) < count:
    if begin % factor == 0:
        l.append(begin)
    begin += 1
print(l)