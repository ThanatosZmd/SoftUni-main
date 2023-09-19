n = int(input())
sum1 = 0
sum2 = 0
for i in range(2*n):
    num = int(input())
    if i<n:
        sum1+=num
    elif i>=n:
        sum2+= num

if sum1==sum2:
    print(f"Yes, sum = {sum1}")
else:
    print(f'No, diff = {abs(sum1-sum2)}')