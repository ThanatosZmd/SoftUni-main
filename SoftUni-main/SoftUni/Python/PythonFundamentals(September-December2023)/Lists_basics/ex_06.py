ints = list(map(int,input().split()))
n = int(input())
for _ in range(n):
    ints.remove(min(ints))
print(*ints, sep=", ")