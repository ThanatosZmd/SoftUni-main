courses = {}
data = input().split(" : ")
while data[0] != "end":
    course = data[0]
    student = data[1]
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(student)
    data = input().split(" : ")

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")