countries = input().split(", ")
capitals = input().split(", ")
data = {countries[i]: capitals[i]
        for i in range(len(countries))}

for key, value in data.items():
    print(f"{key} -> {value}")