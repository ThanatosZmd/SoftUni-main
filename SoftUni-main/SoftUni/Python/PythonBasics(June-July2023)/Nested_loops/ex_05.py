country = input()
saved = 0
while country != 'End':
    needed_money = float(input())
    while True:
        saved += float(input())
        if saved >= needed_money:
            print(f'Going to {country}!')
            break
    country = input()
    saved = 0