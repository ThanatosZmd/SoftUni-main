width = int(input())
length = int(input())
cake = width*length
while True:
    piece_taken = input()
    if piece_taken == 'STOP':
        if cake > 0:
            print(f'{cake} pieces are left.')
        else:
            print(f'No more cake left! You need {abs(cake)} pieces more.')
        break
    else:
        cake -= int(piece_taken)
        if cake < 0:
            print(f'No more cake left! You need {abs(cake)} pieces more.')
            break