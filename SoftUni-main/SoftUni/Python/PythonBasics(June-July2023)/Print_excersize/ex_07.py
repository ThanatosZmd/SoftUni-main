chicken_menus = int(input())*10.35
fish_menus = int(input())*12.4
vegeterian_menus = int(input())*8.15
price = chicken_menus+fish_menus+vegeterian_menus
desert = price*0.2
price+=desert+2.5
print(price)