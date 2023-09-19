time1 = int(input())
time2 = int(input())
time3 = int(input())
total_seconds = time1+time2+time3
secs_left = total_seconds%60
mins = total_seconds//60
if secs_left<10:
    print(f'{mins}:0{secs_left}')
else:
    print(f'{mins}:{secs_left}')