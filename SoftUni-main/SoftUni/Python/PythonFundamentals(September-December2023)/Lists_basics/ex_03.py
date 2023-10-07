A = [1,2,3,4,5,6,7,8,9,10,11]
B = [1,2,3,4,5,6,7,8,9,10,11]
game_terminared = False

card_sequence = input().split()
for el in card_sequence:
    card = el.split("-")
    if card[0] == "A":
        if int(card[1]) in A:
            A.remove(int(card[1]))
    else:
        if int(card[1]) in B:
            B.remove(int(card[1]))
    if len(A) < 7 or len(B) < 7:
        game_terminared = True
        break

print(f"Team A - {len(A)}; Team B - {len(B)}")
if game_terminared:
    print("Game was terminated")