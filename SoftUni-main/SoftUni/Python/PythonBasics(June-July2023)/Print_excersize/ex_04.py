import math
pages = int(input())
page_an_hour = int(input())
days = int(input())

time = pages/page_an_hour
time_day = time/days
print(math.floor(time_day))