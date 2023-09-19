fruit = input()
day = input()
quantity = float(input())

poss_fruits = ['banana','apple','orange','grapefruit','kiwi','pineapple','grapes']
poss_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday']

if not fruit in poss_fruits or not day in poss_days:
    print('error')
    
else:
    if day in week_days:
        if fruit == poss_fruits[0]:
            price = 2.5
        if fruit == poss_fruits[1]:
            price = 1.2
        if fruit == poss_fruits[2]:
            price = 0.85
        if fruit == poss_fruits[3]:
            price = 1.45
        if fruit == poss_fruits[4]:
            price = 2.7
        if fruit == poss_fruits[5]:
            price = 5.5
        if fruit == poss_fruits[6]:
            price = 3.85
    else:
        if fruit == poss_fruits[0]:
            price = 2.7
        if fruit == poss_fruits[1]:
            price = 1.25
        if fruit == poss_fruits[2]:
            price = 0.9
        if fruit == poss_fruits[3]:
            price = 1.6
        if fruit == poss_fruits[4]:
            price = 3
        if fruit == poss_fruits[5]:
            price = 5.6
        if fruit == poss_fruits[6]:
            price = 4.2

    print(f'{(price*quantity):.2f}')