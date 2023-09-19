stay_days = int(input())
room_type = input()
rating = input()

room_price = 0

if room_type == "room for one person":
    room_price = 18.00 * (stay_days - 1)
elif room_type == "apartment":
    room_price = 25.00 * (stay_days - 1)
    if stay_days < 10:
        room_price *= 0.7
    elif 10 <= stay_days <= 15:
        room_price *= 0.65
    else:
        room_price *= 0.5
elif room_type == "president apartment":
    room_price = 35.00 * (stay_days - 1)
    if stay_days < 10:
        room_price *= 0.9
    elif 10 <= stay_days <= 15:
        room_price *= 0.85
    else:
        room_price *= 0.8

if rating == "positive":
    room_price *= 1.25
else:
    room_price *= 0.9

print(f"{room_price:.2f}")
