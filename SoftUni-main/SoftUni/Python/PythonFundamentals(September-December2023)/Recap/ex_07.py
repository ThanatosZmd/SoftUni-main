command = input()
while command!='End':
    new_str = ''
    if command == 'SoftUni':
        command = input()
        continue
    for char in command:
        new_str += char*2
    print(new_str)
    command = input()