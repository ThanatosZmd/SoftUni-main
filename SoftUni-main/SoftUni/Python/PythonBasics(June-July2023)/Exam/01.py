people = int(input())
night = int(input()) * 20
cards = int(input()) * 1.6
tickets = int(input()) * 6
total = people * (night +cards+tickets)
total += total * 0.25
print(f'{total:.2f}')