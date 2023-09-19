flowers = input()
count = int(input())
budget = int(input())

if flowers == "Roses":
    total = count*5
    if count >80:
        total-=0.1*total
elif flowers == "Dahlias":
    total = count*3.8
    if count >90:
        total-=0.15*total
elif flowers == "Tulips":
    total = count*2.8
    if count >80:
        total-=0.15*total
elif flowers == "Narcissus":
    total = count*3
    if count <120:
        total+=0.15*total
elif flowers == "Gladiolus":
    total = count*2.5
    if count <80:
        total+=0.2*total

if budget>=total:
    print(f'Hey, you have a great garden with {count} '
          f'{flowers} and {(budget-total):.2f} leva left.')
else:
    print(f'Not enough money, you need {(total-budget):.2f} leva more.')