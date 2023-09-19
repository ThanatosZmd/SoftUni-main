budget = float(input())
workers = int(input())
price_clothing = float(input())
decor = 0.1*budget
total_clothing = workers*price_clothing

if workers>150:
    total_clothing-=0.1*total_clothing

if budget < total_clothing+decor:
    print("Not enough money!\n"
          f"Wingard needs {((total_clothing+decor) - budget):.2f} leva more.")

else:
    print("Action!\n"
          f"Wingard starts filming with {(budget - (total_clothing + decor)):.2f} leva left.")