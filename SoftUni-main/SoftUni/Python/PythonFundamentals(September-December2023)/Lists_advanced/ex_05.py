rooms = int(input())
free_chairs = 0
error_count = 0
for i in range(1,rooms+1):
    data = input().split()
    chairs = len(data[0])
    visitors = int(data[1])
    if visitors <= chairs:
        free_chairs += chairs - visitors
    else:
        print(f"{visitors-chairs} more chairs needed in room {i}")
        error_count += 1

if error_count == 0:
    print(f"Game On, {free_chairs} free chairs left")