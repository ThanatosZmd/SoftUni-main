budget = float(input())
gpus = int(input())
cpus = int(input())
ram = int(input())

price_gpus = 250*gpus
price_cpus = (0.35*price_gpus)*cpus
price_ram = (0.1*price_gpus)*ram

total = price_gpus + price_cpus + price_ram

if gpus>cpus:
    total = 0.85*total

if budget>=total:
    print(f'You have {(budget-total):.2f} leva left!')
else:
    print(f"Not enough money! You need {(total-budget):.2f} leva more!")