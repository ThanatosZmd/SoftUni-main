actor_name = input()
academy_points = float(input())
n = int(input())

for i in range(n):
    name = input()
    points = float(input())
    academy_points += (len(name)*points)/2
    if academy_points>1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
        break

if academy_points<=1250.5:
    print(f'Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!')