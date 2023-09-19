bad_count = int(input())
excersizes_solved = []
avg_grade = 0
counter = 0
while True:
    excersize = input()
    if excersize != 'Enough':
        grade = int(input())
        avg_grade += grade
        excersizes_solved.append(excersize)
        if grade <=4:
            counter+=1
    else:
        print(f"Average score: {avg_grade/len(excersizes_solved):.2f}\n"
              f'Number of problems: {len(excersizes_solved)}\n'
              f"Last problem: {excersizes_solved[-1]}")
        break
    if counter == bad_count:
        print(f'You need a break, {bad_count} poor grades.')
        break