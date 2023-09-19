floors = int(input())
aps = int(input())

for floor in range(floors,0,-1):
    if floor == floors:
        type = 'L'
    elif floor %2==0:
        type = 'O'
    else:
        type = 'A'
    for room in range(aps):
        print(f'{type}{floor}{room}', end=' ')
    print()