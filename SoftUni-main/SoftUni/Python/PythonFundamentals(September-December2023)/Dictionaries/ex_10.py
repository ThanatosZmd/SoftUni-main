dict = {}
data = input().split(" -> ")
while data[0] != "End":
    company, employee_id = data[0], data[1]
    if company not in dict.keys():
        dict[company] = []
    if employee_id not in dict[company]:
        dict[company].append(employee_id)
    data = input().split(" -> ")

for company, ids in dict.items():
    print(f"{company}")
    for id in ids:
        print(f"-- {id}")