parking_lot = {}
n = int(input())
for i in range(n):
    data = input().split()
    username = data[1]
    if data[0] == "register":
        license_plate = data[2]
        if username in parking_lot.keys():
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif data[0] == "unregister":
        if username not in parking_lot.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking_lot[username]
            print(f"{username} unregistered successfully")

for key, value in parking_lot.items():
    print(f"{key} => {value}")