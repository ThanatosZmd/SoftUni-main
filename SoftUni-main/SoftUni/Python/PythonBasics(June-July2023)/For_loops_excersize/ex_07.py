n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
count = 0

for i in range(n):
    group = int(input())
    if group<=5:
        p1+=group
    elif group>5 and group <=12:
        p2 += group
    elif 12<group<=25:
        p3 += group
    elif 25<group<=40:
        p4 += group
    elif group>=41:
        p5 += group
    count+=group

p1 = (p1/count)*100
p2 = (p2/count)*100
p3 = (p3 / count) * 100
p4 = (p4 / count) * 100
p5 = (p5 / count) * 100

print(f'{p1:.2f}%\n'
      f'{p2:.2f}%\n'
      f'{p3:.2f}%\n'
      f'{p4:.2f}%\n'
      f'{p5:.2f}%')