people = int(input())
season = input()
total = people
if people<=5:
    if season == 'spring':
        total*=50
    elif season == 'summer':
        total*=48.5
        total*=0.85
    elif season == 'autumn':
        total *= 60
    elif season == 'winter':
        total *= 86
        total*=1.08
else:
    if season == 'spring':
        total*=48
    elif season == 'summer':
        total*=45
        total*=0.85
    elif season == 'autumn':
        total *= 49.5
    elif season == 'winter':
        total *= 85
        total*=1.08
print(f'{total:.2f} leva.')