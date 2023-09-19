budget = int(input())
season = input()
fishers = int(input())

if season == "Spring":
    total = 3000
    if fishers <=6:
        total-=0.1*total
    elif fishers <=11:
        total -= 0.15 * total
    elif fishers>=12:
        total -= 0.25*total
elif season == "Summer":
    total = 4200
    if fishers <=6:
        total-=0.1*total
    elif fishers <=11:
        total -= 0.15 * total
    elif fishers>=12:
        total -= 0.25*total
elif season == "Autumn":
    total = 4200
    if fishers <=6:
        total-=0.1*total
    elif fishers <=11:
        total -= 0.15 * total
    elif fishers>=12:
        total -= 0.25*total
elif season == "Winter":
    total = 2600
    if fishers <=6:
        total-=0.1*total
    elif fishers <=11:
        total -= 0.15 * total
    elif fishers>=12:
        total -= 0.25*total

if fishers%2==0 and season!='Autumn':
    total -=0.05*total

if total<=budget:
    print(f'Yes! You have {(budget-total):.2f} leva left.')
else:
    print(f'Not enough money! You need {(total-budget):.2f} leva.')