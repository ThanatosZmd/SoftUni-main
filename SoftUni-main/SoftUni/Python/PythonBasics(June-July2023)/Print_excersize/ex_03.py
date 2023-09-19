deposit = float(input())
months = int(input())
interest = float(input())

price = (deposit + months * ((deposit*(interest/100))/12))
print(price)