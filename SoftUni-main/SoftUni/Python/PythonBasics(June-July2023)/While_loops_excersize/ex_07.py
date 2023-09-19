width = int(input())
length = int(input())
heigth = int(input())
volume = width*heigth*length
while volume >0:
    com = input()
    if com == 'Done':
        if volume>0:
            print(f'{volume} Cubic meters left.')
        else:
            print(f'No more free space! You need {abs(volume)} Cubic meters more.')
        break
    volume-=int(com)
    if volume<=0:
        print(f'No more free space! You need {abs(volume)} Cubic meters more.')
        break