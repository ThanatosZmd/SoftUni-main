n = int(input())
sum1 = 0
sum2 = 0
for i in range(n):
    num = int(input())
    if i%2==0:
        sum1+=num
    else:
        sum2+=num

if sum1==sum2:
    print(f"Yes\nSum = {sum1}")
else:
    print(f'No\nDiff = {abs(sum1-sum2)}')
