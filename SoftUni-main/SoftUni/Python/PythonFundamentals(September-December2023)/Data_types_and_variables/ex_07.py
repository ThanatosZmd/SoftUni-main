capacity = 255
water_in_tank = 0
n = int(input())
for i in range(n):
    water = int(input())
    if capacity-water<0:
        print(f'Insufficient capacity!')
        continue
    capacity-=water
    water_in_tank += water

print(water_in_tank)