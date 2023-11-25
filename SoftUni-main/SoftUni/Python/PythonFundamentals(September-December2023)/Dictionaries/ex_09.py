students = {}
rows = int(input())
for i in range(rows):
    name = input()
    grade = float(input())
    if name not in students.keys():
        students[name] = []
    students[name].append(grade)

final = {name: grade for name, grade in students.items() if sum(students[name]) / len(students[name]) >= 4.5}

for name, grade in final.items():
    print(f"{name} -> {sum(grade)/len(grade):.2f}")