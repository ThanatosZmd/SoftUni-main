name = input()
classes = 1
fails = 0
avg = 0
while True:
    grade = float(input())
    if grade <4:
        fails += 1
        if fails == 2:
            print(f'{name} has been excluded at {classes} grade')
            break
    else:
        avg+=grade
        classes+=1
        if classes >12:
            break


if fails <=1:
    print(f'{name} graduated. Average grade: {avg/12:.2f}')