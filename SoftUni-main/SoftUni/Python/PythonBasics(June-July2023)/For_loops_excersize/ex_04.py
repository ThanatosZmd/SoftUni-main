age = int(input())
price_washing_machine = float(input())
price_toy = int(input())
savings = 0
money_for_bday = 10
toys = 0

for i in range(1,age+1):
    if i%2==0:
        savings += money_for_bday -1
        money_for_bday+=10
    else:
        toys += 1

savings += toys*price_toy
if savings>=price_washing_machine:
    print(f'Yes! {savings-price_washing_machine:.2f}')
else:
    print(f'No! {price_washing_machine-savings:.2f}')