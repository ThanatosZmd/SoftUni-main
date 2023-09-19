sum = input()
total = 0
while True:
    sum = float(sum)
    if sum >= 0:
        total+=sum
        print(f'Increase: {sum:.2f}')
    else:
        print('Invalid operation!')
        break
    sum = input()
    if sum == 'NoMoreMoney':
        break

print(f'Total: {total:.2f}')