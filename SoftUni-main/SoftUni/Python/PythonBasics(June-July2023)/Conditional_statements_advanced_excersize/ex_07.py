month = input()
nights = int(input())

if month == "May" or month == "October":
    studio_price = 50*nights
    apt_price = 65*nights
    if 7<nights<=14:
        studio_price *= 0.95 
    elif nights>14:
        studio_price *= 0.7
        apt_price *= 0.9
if month == 'June' or month == 'Septembber':
    studio_price = 75.2*nights
    apt_price = 68.7*nights
    if nights>14:
        studio_price *= 0.8
        apt_price *= 0.9
elif month == "July" or month == 'August':
    studio_price = 76*nights
    apt_price = 77*nights
    if nights>14:
        apt_price *= 0.9

print(f'Apartment: {apt_price:.2f} lv.\n'
      f"Studio: {studio_price:.2f} lv.")