n = input()
count = 0
for i in range(len(n)):
    if n[i] == 'a':
        count +=1
    elif n[i] == 'e':
        count += 2
    elif n[i] == 'i':
        count += 3
    elif n[i] == 'o':
        count +=4
    elif n[i] == 'u':
        count+=5
print(count)