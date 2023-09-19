divisor = int(input())
boundary = int(input())
n = -1
for i in range(1, boundary+1):
    if i % divisor == 0:
        n = i
print(n)