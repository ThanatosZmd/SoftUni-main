exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

if arrival_time > exam_time:
    print("Late")
    if arrival_time - exam_time < 60:
        print(f"{arrival_time - exam_time} minutes after the start")
    else:
        hours = (arrival_time - exam_time) // 60
        minutes = (arrival_time - exam_time) % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif exam_time - arrival_time <= 30:
    print("On time")
    if exam_time - arrival_time != 0:
        print(f"{exam_time - arrival_time} minutes before the start")
else:
    print("Early")
    if exam_time - arrival_time < 60:
        print(f"{exam_time - arrival_time} minutes before the start")
    else:
        hours = (exam_time - arrival_time) // 60
        minutes = (exam_time - arrival_time) % 60
        print(f"{hours}:{minutes:02d} hours before the start")
