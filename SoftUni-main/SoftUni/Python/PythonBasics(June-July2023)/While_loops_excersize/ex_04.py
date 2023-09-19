step = 0
while True:
    steps = input()
    if steps == 'Going home':
        steps_to_home = int(input())
        step+=steps_to_home
        if step >= 10000:
            print('Goal reached! Good job!\n'
                  f'{step-10000} steps over the goal!')
        else:
            print(f'{10000 - step} more steps to reach goal.')
        break
    else:
        step += int(steps)
    if step >= 10000:
        print('Goal reached! Good job!\n'
              f'{step-10000} steps over the goal!')
        break