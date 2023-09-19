com = input()
min_num = int(com)
while com!='Stop':
    if int(com)<min_num:
        min_num=int(com)
    com = input()

print(min_num)