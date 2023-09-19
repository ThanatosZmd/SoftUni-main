budget = float(input())
season = input()
place = ''
accommodations = ''
price = 0

if budget <= 100:
    place ='Bulgaria'
    if season == 'summer':
        accommodations += "Camp"
        price += 0.3*budget
    elif season == 'winter':
        accommodations += "Hotel"
        price += 0.7*budget
elif budget <=1000:
    place='Balkans'
    if season == 'summer':
        accommodations += "Camp"
        price += 0.4*budget
    elif season == 'winter':
        accommodations += "Hotel"
        price += 0.8*budget
elif budget > 1000:
    place="Europe"
    accommodations = 'Hotel'
    price+=0.9*budget

print(f'Somewhere in {place}\n'
      f'{accommodations} - {price:.2f}')