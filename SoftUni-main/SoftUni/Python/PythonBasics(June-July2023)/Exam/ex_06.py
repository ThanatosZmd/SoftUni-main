K = int(input())
L = int(input())
M = int(input())
N = int(input())

valid_swaps = 0

for i in range(K, 9):
    if valid_swaps > 6:
        break
    for j in range(9,L-1,-1):
        if valid_swaps > 6:
            break
        for k in range(M,9):
            if valid_swaps > 6:
               break
            for l in range(9, N-1, -1):
                if valid_swaps >= 6:
                        break
                #print(f'{i}{j} - {k}{l}')
                if i %2== 0 and j %2 !=0 and k %2 == 0 and l %2 !=0 and ((j!=l) or (i!=k)):
                    print(f'{i}{j} - {k}{l}')
                    valid_swaps+=1
                elif i %2== 0 and j %2 !=0 and k %2 == 0 and l %2 !=0 and ((j==l) or i == k):
                    print('Cannot change the same player.')