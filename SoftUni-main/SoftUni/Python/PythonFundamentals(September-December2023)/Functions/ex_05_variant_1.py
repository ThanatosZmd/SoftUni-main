is_even = lambda x: x%2==0
print(list(filter(is_even, list(map(int,input().split())))))