money_needed = float(input())
money_available = float(input())
counter = 0
days = 1
while True:
    action = input()
    sum = float(input())
    if action == 'spend':
        counter += 1
        if counter == 5:
            print('You can\'t save the money.\n'
                  f'{days}')
            break
        money_available-=sum
        if money_available<=0:
            money_available = 0
    if action == 'save':
        money_available+=sum
        counter = 0
    if money_available>=money_needed:
        print(f'You saved the money for {days} days.')
        break
    days+=1