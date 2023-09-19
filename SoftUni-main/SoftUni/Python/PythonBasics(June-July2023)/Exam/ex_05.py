days = 1
current = 5364
top = 8848
is_Top = False
while True:
    command = input()
    if command == 'END':
        break
    elif command == 'Yes':
        days += 1
    elif command == 'No':
        pass

    current += int(input())
    if current >= top:
        is_Top = True
        break
    if days >= 5:
        break

if is_Top:
    print(f'Goal reached for {days} days!')
else:
    print('Failed!\n'
          f'{current}')