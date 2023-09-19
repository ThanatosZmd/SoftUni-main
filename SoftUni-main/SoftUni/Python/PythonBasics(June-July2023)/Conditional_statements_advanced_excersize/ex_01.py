type_film = input()
rows=  int(input())
columns = int(input())

if type_film == "Premiere":
    price = rows * columns * 12.00
    print(f'{price:.2f} leva')
elif type_film == "Normal":
    price = rows*columns*7.5
    print(f'{price:.2f} leva')
else:
    price = rows*columns*5
    print(f'{price:.2f} leva')