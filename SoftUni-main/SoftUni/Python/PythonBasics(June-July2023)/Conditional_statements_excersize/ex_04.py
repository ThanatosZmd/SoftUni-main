price_excursion=float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_earnings = puzzles*2.6 + dolls*3 + bears*4.1 + minions*8.2 + trucks*2
orders = puzzles+dolls+bears+minions+trucks

if orders>=50:
    total_earnings-=0.25*total_earnings

total_earnings-=0.1*total_earnings

if total_earnings>=price_excursion:
    print(f"Yes! {(total_earnings-price_excursion):.2f} lv left.")
else:
    print(f"Not enough money! {(price_excursion-total_earnings):.2f} lv needed.")