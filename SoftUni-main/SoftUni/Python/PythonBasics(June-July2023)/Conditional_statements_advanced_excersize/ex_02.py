weather = int(input())
time = input()

if time == 'Morning':
    if 10<=weather<=18:
        print(f'It\'s {weather} degrees, get your Sweatshirt and Sneakers.')
    elif 18<weather<=24:
        print(f'It\'s {weather} degrees, get your Shirt and Moccasins.')
    else:
        print(f'It\'s {weather} degrees, get your T-Shirt and Sandals.')
elif time == 'Afternoon':
    if 10<=weather<=18:
        print(f'It\'s {weather} degrees, get your Shirt and Moccasins.')
    elif 18<weather<=24:
        print(f'It\'s {weather} degrees, get your T-Shirt and Sandals.')
    else:
        print(f'It\'s {weather} degrees, get your Swim Suit and Barefoot.')
elif time == 'Evening':
    if 10<=weather<=18:
        print(f'It\'s {weather} degrees, get your Shirt and Moccasins.')
    elif 18<weather<=24:
        print(f'It\'s {weather} degrees, get your Shirt and Moccasins.')
    else:
        print(f'It\'s {weather} degrees, get your Shirt and Moccasins.')