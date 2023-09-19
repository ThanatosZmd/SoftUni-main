students = int(input())
top = 0
between_4_5 = 0
between_3_4 = 0
fails = 0
avg_grade = 0

for i in range(students):
    grade = float(input())
    if grade < 3:
        fails+=1
    elif grade < 4:
        between_3_4 += 1
    elif grade <5:
        between_4_5 += 1
    else:
        top += 1
    avg_grade += grade

avg_grade /= students
top = top/students * 100
between_4_5 = (between_4_5 / students) * 100
between_3_4 = (between_3_4/students)*100
fails = (fails/(students))*100 
print(f'Top students: {top:.2f}%\n'
      f'Between 4.00 and 4.99: {between_4_5:.2f}%\n'
      f'Between 3.00 and 3.99: {between_3_4:.2f}%\n'
      f'Fail: {fails:.2f}%\n'
      f'Average: {avg_grade:.2f}')