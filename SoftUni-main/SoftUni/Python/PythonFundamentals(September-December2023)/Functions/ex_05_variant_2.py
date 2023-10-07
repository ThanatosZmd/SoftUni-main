y = list(map(int,input().split()))
def is_even(a):
    if a%2==0:
        return True
    return False
result =[]
for i in range(len(y)):
      if is_even(y[i]):
            result.append(y[i])
print(result)


