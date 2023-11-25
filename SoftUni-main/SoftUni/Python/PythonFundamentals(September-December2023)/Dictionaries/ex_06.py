products = {}
data = input().split(" ")
while data[0] != "buy":
    key = data[0]
    values = [float(data[1]),int(data[2])]
    if key not in products.keys():
        products[key] = values
    else:
        products[key][1] += values[1]
        if products[key][0] != values[0]:
            products[key][0] = values[0]
    data = input().split()

for key, values in products.items():
    print(f"{key} -> {values[1]*values[0]:.2f}")