import math

n = int(input())
points = int(input())
avg = 0
wins = 0
for i in range(n):
    stage = input()
    if stage == "W":
        points += 2000
        avg += 2000
        wins += 1
    elif stage == 'F':
        points += 1200
        avg += 1200
    elif stage == "SF":
        points += 720
        avg += 720

avg = (avg/n)

print(f'Final points: {points}\n'
      f'Average points: {math.floor(avg)}\n'
      f'{(wins/n)*100:.2f}%')
    