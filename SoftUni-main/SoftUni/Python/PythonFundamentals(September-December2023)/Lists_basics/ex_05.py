cards = input().split()
cards_total = len(cards)
half_total = cards_total//2
faro_shuffles = int(input())

first_half = cards[:half_total]
second_half = cards[half_total:]
new_order = cards
for _ in range(faro_shuffles):
    for i in range(half_total):
        new_order[i*2] = first_half[i]
        new_order[i*2+1] = second_half[i]
    first_half = new_order[:half_total]
    second_half = new_order[half_total:]
print(new_order)