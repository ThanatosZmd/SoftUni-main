import math

tv_series = str(input())
episode_time = int(input())
break_time = int(input())

break_time -= (0.25*break_time + 0.125*break_time)

if break_time >= episode_time:
    print(f"You have enough time to watch {tv_series} and left with {math.ceil(break_time-episode_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_series}, you need {math.ceil(episode_time-break_time)} more minutes.")