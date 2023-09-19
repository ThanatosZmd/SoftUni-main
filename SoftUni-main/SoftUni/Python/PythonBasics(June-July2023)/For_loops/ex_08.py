n = int(input())
num = int(input())
max_num = num
min_num = num
for i in range(n-1):
    num = int(input())
    if num > max_num:
        max_num = num
    if num<min_num:
        min_num = num

print(f'Max number: {max_num}\n'
      f'Min number: {min_num}')