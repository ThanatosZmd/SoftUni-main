a = int(input())
b = int(input())+1
num = int(input())
is_num = False
counter = 0
for i in range(a,b):
    if is_num:
        break
    for j in range(a,b):
        counter += 1
        if i + j == num:
            is_num = True
            print(f'Combination N:{counter} '
                  f'({i} + {j} = {num})')
            break
if not is_num:
    print(f'{counter} combinations - neither equals {num}')