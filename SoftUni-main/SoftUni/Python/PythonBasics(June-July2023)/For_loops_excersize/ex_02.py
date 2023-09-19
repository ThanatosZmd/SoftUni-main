n = int(input())
l = []

for i in range (n):
    num = int(input())
    l.append(num)

if max(l) == sum(l)-max(l):
    print(f'Yes\nSum = {max(l)}')
else:
    print(f'No\nDiff = {abs(max(l) - (sum(l)-max(l)))}')