n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())
    if num<200:
        p1+=1
    elif 200<=num<=399:
        p2+=1
    elif 400<=num<=599:
        p3+=1
    elif 600<=num<=799:
        p4+=1
    else:
        p5 += 1

p1 = (p1/n)*100
p2 = (p2/n)*100
p3 = (p3/n)*100
p4 = (p4/n)*100
p5 = (p5 / n) * 100

print(f'{p1:.2f}%\n'
      f'{p2:.2f}%\n'
      f'{p3:.2f}%\n'
      f'{p4:.2f}%\n'
      f'{p5:.2f}%')