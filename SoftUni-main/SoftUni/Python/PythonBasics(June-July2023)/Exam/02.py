price_party = float(input())
love_letters = int(input())
roses = int(input())
keychains = int(input())
caaricatures = int(input())
suprizes = int(input())
total_orders = love_letters+roses+keychains+caaricatures+suprizes
total_sales = love_letters*0.6+roses*7.2+keychains*3.6 + caaricatures*18.2+suprizes*22
if total_orders >= 25:
    total_sales *= 0.65
total_sales*=0.9

if total_sales>=price_party:
    print(f'Yes! {total_sales-price_party:.2f} lv left.')
else:
    print(f'Not enough money! {price_party-total_sales:.2f} lv needed.')