tabs = int(input())
wage = float(input())

for i in range(tabs):
    tab = input()
    if tab == "Facebook":
        wage -= 150
    elif tab == 'Reddit':
        wage -= 50
    elif tab == 'Instagram':
        wage -= 100
    if wage <=0:
        break

if wage <=0:
    print("You have lost your salary.")
else:
    print(f'{wage:.0f}') 