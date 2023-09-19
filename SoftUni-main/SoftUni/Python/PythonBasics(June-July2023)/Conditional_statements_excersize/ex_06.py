import math
world_record = float(input())
meters = float(input())
seconds_per_meter = float(input())
total_time = seconds_per_meter*meters
total_time+= (meters//15)*12.5
math.floor(total_time)
if total_time<world_record:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(total_time-world_record):.2f} seconds slower.")