naylon = (int(input())+2)*1.5 
paint = int(input())
total_paint = (paint+(0.1*paint))*14.5
thinner = int(input())*5
hours = int(input())
total_price_materials = naylon+total_paint+thinner+0.4
workers_price = (total_price_materials*0.3)*hours
print(total_price_materials+workers_price)