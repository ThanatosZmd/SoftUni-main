n = int(input())
bonus_points = 0
if n<=100:
    bonus_points+=5
elif n>100 and n<=1000:
    bonus_points+=0.2*n
elif n>1000:
    bonus_points+=0.1*n
if n%2==0:
    bonus_points+=1
if n%5==0 and n%2==1:
    bonus_points+=2
print(bonus_points)
print(n+bonus_points)