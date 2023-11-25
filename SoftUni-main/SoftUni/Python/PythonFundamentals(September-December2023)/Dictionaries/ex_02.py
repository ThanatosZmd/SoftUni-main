resource = input()
resources = {}
while resource != "stop":
    if resource not in resources.keys():
        resources[resource] = 0
    quantity = int(input())
    resources[resource] += quantity
    resource = input()

for key, value in resources.items():
    print(f"{key} -> {value}")
