data = list(input())
for i in range(len(data)):
    data[i] = chr(ord(data[i])+3)
print("".join(data))